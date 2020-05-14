import sys
import berserk
import chess

import Game


try:
    with open("..\\key.txt") as f:
        token = f.read()
    session = berserk.TokenSession(token)
    client = berserk.clients.Client(session)
    board = berserk.clients.Board(session)
except:
    print("The API-key is either empty or wrong. Please run the command 'lichesskey' and input your API-key correctly. If you need more help, please see the instructions in the Github README: \nhttps://github.com/Cqsi/lichess_terminal#how-to-generate-a-personal-api-token")
    os._exit(0)

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