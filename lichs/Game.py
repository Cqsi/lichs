import threading
import datetime
import chess

import os

chess_board = chess.Board()
runOnce = True

class Game(threading.Thread):

    display_map = {
        'P': ['♟', '♙'],
        'R': ['♜', '♖'],
        'N': ['♞', '♘'],
        'B': ['♝', '♗'],
        'Q': ['♛', '♕'],
        'K': ['♚', '♔'],
        'p': ['♙', '♟'],
        'r': ['♖', '♜'],
        'n': ['♘', '♞'],
        'b': ['♗', '♝'],
        'q': ['♕', '♛'],
        'k': ['♔', '♚']
    }

    def __init__(self, board, game_id, player_id, isWhite, color, time, enhanced_display, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.board = board
        self.stream = board.stream_game_state(game_id)
        self.player_id = player_id
        self.isWhite = isWhite
        self.color = color
        self.clock = {'white': datetime.datetime(1970, 1, 1, 0, time, 0), 'black': datetime.datetime(1970, 1, 1, 0, time, 0)}
        self.first_move = 2 # returns false after 2 moves have been made
        self.enhanced_display = enhanced_display
        if self.isWhite:
            self.white_first_move()


    def run(self):
        for event in self.stream:
            if event['type'] == "gameFull":
                self.handle_game_full(event)
            elif event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):

        global chess_board

        if game_state.get(self.color[0].lower() + "draw") is True:
            self.handle_draw_state(game_state)
        elif game_state["status"] == "resign":
            print("The opponent resigned. Congrats!")
            os._exit(0)

        else:
            # update time
            self.clock['white'] = game_state['wtime']
            self.clock['black'] = game_state['btime']

            # there's no "amount of turns" variable in the JSON, so we have to construct one manually
            turn = len(game_state["moves"].split())-1
            if turn%2 == self.isWhite:

                print(self.color + " moved.")
                print()

                chess_board.push_uci(game_state["moves"].split()[-1])
                self.display_board()
                print()

                # decrement first move counter
                if self.first_move:
                    self.first_move -= 1

                self.check_mate(chess_board)

                # user move start time
                move_start = datetime.datetime.now()

                while(True):
                    try:
                        move = input("Make your move: ")
                        if move.lower() == "resign":
                            self.board.resign_game(self.game_id)
                            print("You resigned the game!")
                            print("Thanks for playing!")
                            os._exit(0)
                        else:
                            self.board.make_move(self.game_id, chess_board.parse_san(move))
                            chess_board.push_san(move)
                            if self.first_move:
                                self.first_move -= 1
                            elif self.color[0] == 'b':
                                self.clock['white'] -= datetime.datetime.now() - move_start
                            else:
                                self.clock['black'] -= datetime.datetime.now() - move_start
                    except Exception as e:
                        print("You can't make that move. Try again!")
                        print(f"Reason: {e}") 
                        continue
                    break

                self.display_board()
                self.check_mate(chess_board)
                print()
                print(self.color + "'s turn...")

    def handle_game_full(self, gamefull):
        # TODO Write this method
        pass

    def handle_draw_state(self, game_state):
        # TODO Write this method
        pass

    def handle_chat_line(self, event):
        # TODO Write this method
        pass

    def white_first_move(self):

        global chess_board

        self.display_board()
        while(True):
            try:
                move = input("Make your move: ")
                if move.lower() == "resign":
                    self.board.resign_game(self.game_id)
                    os._exit(0)
                else:
                    self.board.make_move(self.game_id, chess_board.parse_san(move))
                    chess_board.push_san(move)
            except Exception as e:
                print("You can't make that move. Try again!")
                print(f'Reason: {e}')
                continue
            break

        self.display_board()
        self.first_move -= 1
        print(self.color + "'s turn...")

    def check_mate(self, chess_board):
        if str(chess_board.result()) != "*":
            if chess_board.result() == "1-0":
                if self.isWhite:
                    print("Congrats! You won by checkmating your opponent!")
                else:
                    print("You lose! Your opponent has checkmated you!")
            elif chess_board.result() == "0-1":
                if self.isWhite:
                    print("You lose! Your opponent has checkmated you!")
                else:
                    print("Congrats! You won by checkmating your opponent!")
            elif chess_board.result() == "1/2-1/2":
                print("The game ended in a stalemate (draw)!")

            print("Thanks for playing!")
            os._exit(0)

    def enhance_board_display(self, board_str: str) -> str:
        """Takes the standard board display from chess and modifies it to use symbols and add annotations

        :param board_str: a string board display coming out of chess.Board
        :return: Enhanced board display using emojis and adding rank and file labels
        """
        white_back = "\u001b[47m"
        black_back = "\u001b[40m"
        white_txt = "\u001b[37m"
        black_txt = "\u001b[30m"
        # make into list of row strings
        board_rows = board_str.split('\n')
        # make into matrix of chars
        board_rows = [row.split(' ') for row in board_rows]

        # replace matrix elements with checkered squares and icons
        new_board = []
        black = True
        for row in board_rows:
            new_row = []
            for item in row:
                if black:
                    new_row.append(f'{black_back}{white_txt}{self.display_map.get(item, [" "])[0]}')
                    black = False
                else:
                    new_row.append(f'{white_back}{black_txt}{self.display_map.get(item, ["", " "])[1]}')
                    black = True
            new_board.append(new_row)
            black = not black

        board_rows = new_board

        # Add numbers and letters to side and bottom of board
        if self.isWhite:
            board_rows = [row + [f'{black_back}{white_txt} {abs(i)}'] 
                          for i, row in enumerate(board_rows, start=-len(board_rows))]
            board_rows.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        else:
            board_rows = [row + [f'{black_back}{white_txt} {i}'] for i, row in enumerate(board_rows, start=1)]
            board_rows.append(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])

        board_rows = [' '.join(row) for row in board_rows]
        return '\n'.join(board_rows)


    def display_board(self):
        global chess_board

        # display the chess board, if the the player's color is black then flip the board 
        if self.isWhite:
            board_str = str(chess_board)
        else:
            board_str = str(chess_board.transform(chess.flip_vertical).transform(chess.flip_horizontal))

        if self.enhanced_display:
            print(self.enhance_board_display(board_str))
        else:
            print(board_str)

        # print clock
        print("[%02d:%02d : %02d:%02d]" % (self.clock['white'].minute, self.clock['white'].second,
                                           self.clock['black'].minute, self.clock['black'].second))
        print()

