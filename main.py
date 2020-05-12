import sys
import berserk
import chess

import Game

# change path before release
with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.clients.Client(session)
board = berserk.clients.Board(session)

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

board.seek(time, 0)
print("Searching after opponent...")

for event in board.stream_incoming_events():
    if event['type'] == 'gameStart':

        print("An opponent was found!")

        isWhite = True
        color = "Black" # We set the color to the opposite color of the player
        
        if player_id != client.games.export(event['game']['id'])['players']['white']['user']['id']:
            isWhite = False
            color = "White"
            print("White's turn...")
        game = Game.Game(board, event['game']['id'], player_id, isWhite, color)
        game.start()