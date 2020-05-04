import berserk
import chess
import threading

class Game(threading.Thread):
    def __init__(self, client, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        print("State changed")

    def handle_chat_line(self, chat_line):
        pass

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.Client(session)

# Gets your account data, e.g ["id"], ["username"]
account_data = client.account.get()
#print(account_data)

is_polite = True
for event in client.bots.stream_incoming_events():
    if event['type'] == 'challenge':
        client.bots.accept_challenge(event['challenge']['id'])
    elif event['type'] == 'gameStart':
        print(event)
        game = Game(client, event['game']['id'])
        game.start()

