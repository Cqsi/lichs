import berserk
import chess
import threading

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.clients.Client(session)
board = berserk.clients.Board(session)

class Game(threading.Thread):
    def __init__(self, board, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.board = board
        self.stream = board.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        print("White moved!!!")

    def handle_chat_line(self, chat_line):
        pass


# Gets your account data, e.g ["id"], ["username"]
account_data = client.account.get()
#print(account_data)

is_polite = True
for event in board.stream_incoming_events():
    if event['type'] == 'challenge':
        print("Challenge time!!!")

        # Accepts the challenge, mainly used for testing
        game_id = event['challenge']['id']
        board.accept_challenge(game_id)

        # Post message in chat
        #board.post_message(game_id, "Hello noob!")
    elif event['type'] == 'gameStart':
        game = Game(board, event['game']['id'])
        game.start()