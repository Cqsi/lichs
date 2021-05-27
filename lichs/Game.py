import threading
import chess

import os

chess_board = chess.Board()
runOnce = True

class Game(threading.Thread):

    def __init__(self, board, game_id, player_id, isWhite, color, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.board = board
        self.stream = board.stream_game_state(game_id)
        self.player_id = player_id
        self.isWhite = isWhite
        self.color = color
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

        if game_state[self.color[0].lower() + "draw"] == True:
            self.handle_draw_state(game_state)
        elif game_state["status"] == "resign":
            print("The opponent resigned. Congrats!")
            os._exit(0)

        else:
            # there's no "amount of turns" variable in the JSON, so we have to construct one manually
            turn = len(game_state["moves"].split())-1
            if turn%2 == self.isWhite:

                print(self.color + " moved.")
                print()

                chess_board.push_uci(game_state["moves"].split()[-1])
                self.display_board()
                print()

                self.check_mate(chess_board)

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
                    except:
                        print("You can't make that move. Try again!")
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
            except:
                print("You can't make that move. Try again!")
                continue
            break

        self.display_board()
        print()
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

    def display_board(self):
        global chess_board

        # display the chess board, if the the player's color is black then flip the board 
        if self.isWhite:
            print(chess_board)
        else:
            print(chess_board.transform(chess.flip_vertical).transform(chess.flip_horizontal))