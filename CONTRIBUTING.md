## Contributing
If you want to play around with the library, go ahead, it's open-source! I would be really happy if anybody could improve the program.

If you want to test the program, without starting a game against a real player, it's a little tricky. You basically need to create a new account on Lichess, and then go into the `lichs/testing` folder. There you will find pretty much the exact same copy of the `main.py` and `Game.py` files. Put your API-key in the `main_test.py` file (on the token variable found in the file). Now trying running the main_test file. It should throw an error. This is because of an issue with the berserk API that I'm using to connect Python to Lichess. If you go and check out [berserk](https://github.com/rhgrant10/berserk) and into berserk/clients you will find that under the Board class there is no method for accepting a challenge. So here's what you have to do:

1. Clone (locally) [my version of berserk](https://github.com/Cqsi/berserk) containing a method in the Board class for accepting challenges
2. When finished cloning, go into that folder and type `pip install .`. Now you're just essentially installing a python package, except that it isn't from PyPi, it's from your local machine.
3. That's it!

When you then run the `main_test.py` file, nothing will happen, and this is okay. Now you go on another Lichess account, and then when you invite this account (the account with the API-key in the program) to a game, it will accept automatically and the game will start. This way you can test whatever changes you make. The `Game.py` and `Game_test.py` files are the same, so if you're happy you should be able to just copy your changes.

### Useful links 
* https://berserk.readthedocs.io/en/master/installation.html - Python client for the Lichess API
* https://lichess.org/api - Lichess API
* https://lichess.org/api#tag/Board - Lichess Board API
* https://python-chess.readthedocs.io/en/latest/ - python-chess library