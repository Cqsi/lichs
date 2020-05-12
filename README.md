# Lichess Terminal

## Info
* Version v1.0
* <ins>Uses Lichess</ins>, which means that you need to have a Lichess account
* Operating System: Only Windows for now (see [TODO](https://github.com/Cqsi/lichess_terminal#todo-and-current-questions))

Lichess Terminal uses the Lichess API (more exactly [berserk](https://github.com/rhgrant10/berserk)) to make it possible for you to play against other real players directly in the terminal on Lichess servers. <ins>This project is still in its early stages; there's no chat support, pretty bad graphics and probably some bugs.</ins>

## Installation
this is the installation section.

## Usage
this is the usage section.



## How to contribute?
### TODO and Current Questions
* This program only works on Windows at the moment, can anyone make the Linux and macOS equivalent of the batch-file found in the `batch` folder?
* The chessboard that is displayed isn't very nice looking (it's just letters and dots!), but I'm unsure whether CMD allows much better graphics. The goal would be to create something like [this](https://www.reddit.com/r/chess/comments/cm394n/play_chess_against_stockfish_in_your_terminal/) on other systems like Linux for example.
* Make it so that the user can see the chat, maybe in an another terminal window. My plan was to create a second command (e.g. "lichess chat) so that you can open a second terminal window and type the command and then get the chat displayed.
* How do you change the POV (Point Of View) of the chessboard in python-chess? Is it even possible? The current program displays everything from the white's side so if you're black it might be a little weird.

### Useful links 
* https://lichess.org/api - Lichess API
* https://lichess.org/api#operation/apiBoardSeek - Create a "seek", match vs random player, lichess API
* https://berserk.readthedocs.io/en/master/installation.html - Python client for the Lichess API
* https://lichess.org/api#tag/Board - Lichess Board API
* https://chess.stackexchange.com/questions/28870/render-a-chessboard-from-a-pgn-file - How to save the python-chess board as an SVG-image