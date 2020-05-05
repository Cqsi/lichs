import berserk
import chess

import Game

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.clients.Client(session)
board = berserk.clients.Board(session)

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
        game = Game.Game(board, event['game']['id'])
        game.start()