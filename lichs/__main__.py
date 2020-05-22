import sys
import os
import berserk
import chess
from pathlib import Path

#from .Game import Game
#from .api_key import set_api

from lichs.Game import Game
from lichs.api_key import set_api

token_file = Path(__file__).parent.absolute() / "key"


def set_token(key):
    token_file.write_text(key)
    print("The API-token " + key + " was entered and saved.")



def main():
    if len(sys.argv) == 2:
            set_token(sys.argv[1])

    if not token_file.exists():
        print("Please provid a token key")
        print("See the instructions in the Github README:")
        print("https://github.com/Cqsi/lichs#how-to-generate-a-personal-api-token")
        key = input("token: ")
        set_token(key)

    try:
        token = token_file.read_text()
        session = berserk.TokenSession(token)
        client = berserk.clients.Client(session)
        board = berserk.clients.Board(session)
    except:
        print("Unable to connect Lichess")
        print("Check if your token key is right")
        print("Or try again later")
        os._exit(0)

    # Gets your account data, e.g ["id"], ["username"]
    account_data = client.account.get()
    player_id = account_data["id"]

    # Welcome text
    print("Welcome to Lichess!\n")
    print("What kind of chess do you want to play?")
    print("1. Rapid (10+0)\n2. Classical (30+0)\n")
    num = input("Enter 1 or 2: ")
    time = 0

    if num=="1":
        time=10
    elif num=="2":
        time=30
    else:
        # This needs improvement, something like a while/for loop
        print("Something went wrong, please enter the lichess command again.")
        sys.exit()

    print("Searching after opponent...")
    board.seek(time, 0)

    for event in board.stream_incoming_events():
        if event['type'] == 'gameStart':

            print("An opponent was found!")

            isWhite = True
            color = "Black" # We set the color to the opposite color of the player
                
            if player_id != client.games.export(event['game']['id'])['players']['white']['user']['id']:
                isWhite = False
                color = "White"
                print("You're playing as black!")
                print("White's turn...")
            else:
                print("You're playing as white!")
            game = Game(board, event['game']['id'], player_id, isWhite, color)
            game.start()
