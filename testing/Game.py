import threading
import chess

import sys

chess_board = chess.Board()
color = "Black"
move_arr = []
runOnce = True

class Game(threading.Thread):

    def __init__(self, board, game_id, player_id, isWhite, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.board = board
        self.stream = board.stream_game_state(game_id)
        self.current_state = next(self.stream)
        self.player_id = player_id
        self.isWhite = isWhite

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        
        # big spaghetti code alert, horrible code below needs improvement
        # TODO: What if you're white?

        global chess_board
        global color
        global move_arr

        if game_state[color[0].lower() + "draw"] == True:
            handle_draw_state(game_state)
        elif game_state["status"] == "resigned":
            print("The oppononent resigned. Congrats!")
            sys.exit()
            # TODO make another file for "seeking" so that the player can choose if he/she wants to play again
            # for now, just quit

        elif len(game_state["moves"].split())-1 == len(move_arr):
            if len(game_state["moves"].split())%2==self.isWhite: 
                
                print(color + " moved.")
                print()
                
                chess_board.push_uci(game_state["moves"].split()[-1])
                print(chess_board)
                print()
                move_arr.append(game_state["moves"].split()[-1])

            else:
                move = input("Make your move: ")
                move_arr.append(move)
                self.board.make_move(self.game_id, move)
                chess_board.push_uci(move)
                print(chess_board)
                print()
                print(color + "'s turn...")
            
        else:
            # I believe this case is when the opponent has canceled the game
            print("The opponent canceled the game.")
            sys.exit()

    def handle_chat_line(self, chat_line):
        # TODO write this method
        pass

    def handle_draw_state(self, game_state):
        # TODO write this method
        pass