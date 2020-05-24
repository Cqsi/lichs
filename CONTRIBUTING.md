## Contributing
If you want to play around with the library, go ahead, it's open-source! I would be really happy if anybody could improve the program (see the TODOs below). 

If you want to test the program, without starting a game against a real player, it's a little tricky. You basically need to create a new account on Lichess, and then go into the `lichs/testing` folder. There you will find pretty much the exact same copy of the `main.py` and `Game.py` files. To specify the API-key in the `main.py` file, you can just use absolute paths to the file containing the API-key, but it really doesn't matter. Then you can run `main.py`, which waits until it gets challenged and then accepts the challenge. This way you can send a challenge from your "real" account and then the program accepts it, which means that you can play against yourself, one from the terminal and the other from the webpage.

### TODO and Current Questions
Down below are a few TODO's, but you should also check out the [issue page](https://github.com/Cqsi/lichs/issues).
* Add ability to offer a draw
* Add ability for user to see how much time he/she has left
* Add support for ranked games
* The chessboard that is displayed isn't very nice looking (it's just letters and dots!), but I'm unsure whether CMD allows much better graphics. The goal would be to create something like [this](https://www.reddit.com/r/chess/comments/cm394n/play_chess_against_stockfish_in_your_terminal/) on other systems like Linux for example.
* Make it so that the user can see the chat, maybe in an another terminal window. My plan was to create a second command (e.g. "lichess chat) so that you can open a second terminal window and type the command and then get the chat displayed.

### Useful links 
* https://berserk.readthedocs.io/en/master/installation.html - Python client for the Lichess API
* https://lichess.org/api - Lichess API
* https://lichess.org/api#tag/Board - Lichess Board API
* https://python-chess.readthedocs.io/en/latest/ - python-chess library