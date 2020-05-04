import berserk
import chess

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.Client(session)

# Gets your account data, e.g ["id"], ["username"]
account_data = client.account.get()
#print(account_data)

is_polite = True
for event in client.bots.stream_incoming_events():
    print(event)
    if event['type'] == 'challenge':
        client.bots.accept_challenge(event['challenge']['id'])
    elif event['type'] == 'gameStart':
        game = Game(event['id'])
        game.start()