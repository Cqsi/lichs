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
        self.current_state = next(self.stream)
        self.player_id = player_id
        self.isWhite = isWhite
        self.color = color
        if self.isWhite:
            self.white_first_move()


    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        
        # big spaghetti code alert, if anyone comes up with a better way to this method please submit your code

        global chess_board

        if game_state[self.color[0].lower() + "draw"] == True:
            self.handle_draw_state(game_state)
        elif game_state["status"] == "resign":
            print("The oppononent resigned. Congrats!")
            os._exit(0)
            # TODO make another file for "seeking" so that the player can choose if he/she wants to play again
            # for now, just quit

        else:
            if (len(game_state["moves"].split())-1)%2==self.isWhite: 

                print(self.color + " moved.")
                print()
                
                chess_board.push_uci(game_state["moves"].split()[-1])
                print(chess_board)
                print()

                while(True):
                    try:
                        move = input("Make your move: ")
                        self.board.make_move(self.game_id, move)
                        chess_board.push_uci(move)
                    except:
                        print("You can't make that move. Try again!")
                        continue
                    break
                
                print(chess_board)
                print()
                print(self.color + "'s turn...")


    def handle_draw_state(self, game_state):
        # TODO Write this method
        pass
    
    def white_first_move(self):

        global chess_board

        print(chess_board)
        while(True):
            try:
                move = input("Make your move: ")
                self.board.make_move(self.game_id, move)
                chess_board.push_uci(move)
            except:
                print("You can't make that move. Try again!")
                continue
            break
        print(chess_board)
        print()
        print(self.color + "'s turn...")

    def check_mate(chess_board):
        if chess_board.result != "*":
            if chess_board.result == "1-0":
                if self.isWhite:
                    print("Congrats! You won by checkmating your opponent!")
                else:
                    print("You lose! Your opponent has checkmated you!")
            elif chess_board.result == "0-1":
                if self.isWhite:
                    print("You lose! Your opponent has checkmated you!")
                else:
                    print("Congrats! You won by checkmating your opponent!")
            elif chess_board.result == "1/2-1/2":
                print("The game ended in a stalemate (draw)!")
            print("Thanks for playing!")
            os._exit(0)