# Lichess in terminal

## Links 
* https://lichess.org/api - Lichess API
* https://lichess.org/api#operation/apiBoardSeek - Create a "seek", match vs random player, lichess API
* https://berserk.readthedocs.io/en/master/installation.html - Python client for lichess
* https://lichess.org/api#tag/Board - Lichess Board API
* https://chess.stackexchange.com/questions/28870/render-a-chessboard-from-a-pgn-file - How to save the python-chess board as an SVG-image

## TODO
* Fix the code in `game.py`, so that the starting color doen't matter.
* Switch the board in python-chess depending on what color you are (how to do this?)
* ~~Create a "seek" (search for opponent) on demand~~
* ~~Create batch files for commands~~
* Copy the current files to another folder so one could test the commands and everything playing against oneself instead of against a real player
* Is the `handle_game_state` (in `game.py`) method reacting to other stuff than moves (draw requsts?)
* Make try/excep. statements so that the program doesn't crash when the user enters the wrong information (e.g. a move)
