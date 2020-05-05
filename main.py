import berserk
import chess
import threading

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
        board.accept_challenge(event['challenge']['id'])
#    elif event['type'] == 'gameStart':
#        #print(event)
#        game = Game(client, event['game']['id'])
#        game.start()