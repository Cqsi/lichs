import sys
import berserk
import chess

import Game


# Read the Lichess API token
with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.clients.Client(session)
board = berserk.clients.Board(session)

# Gets your account data, e.g ["id"], ["username"]
account_data = client.account.get()
player_id = account_data["id"]

for event in board.stream_incoming_events():
    if event['type'] == 'challenge':
        print("Challenge time!!!")

        # Accepts the challenge, mainly used for testing
        game_id = event['challenge']['id']
        board.accept_challenge(game_id)

    elif event['type'] == 'gameStart':

        #print(client.games.export(event['game']['id']))
        isWhite = True
        color = "Black" # We set the color to the opposite color of the player

        if player_id != client.games.export(event['game']['id'])['players']['white']['user']['id']:
            isWhite = False
            color = "White"
            print("You're playing as black!")
            print("White's turn...")
        else:
            print("You're playing as white!")
        game = Game.Game(board, event['game']['id'], player_id, isWhite, color)
        game.start()