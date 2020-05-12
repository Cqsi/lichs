# Lichess Terminal

## Info
* Version v1.0
* <ins>Uses Lichess</ins>, which means that you need to have a Lichess account
* Operating System: Only Windows for now (see [TODO](https://github.com/Cqsi/lichess_terminal#todo-and-current-questions))
* Only Classical and Rapid games because the Lichess API doesn't allow anything else

Lichess Terminal uses the Lichess API (more exactly [berserk](https://github.com/rhgrant10/berserk)) to make it possible for you to play against other real players directly in the terminal on Lichess servers. <ins>This project is still in its early stages; there's no chat support, pretty bad graphics, no ranked games and probably some bugs.</ins>

## Installation
this is the installation section.

## Usage
You start playing by typing the command `lichess` into the Windows Command Prompt:

```
C:\> lichess
```

That will take you to the intro screen:

```
Welcome to Lichess!

What kind of chess do you want to play?
1. Rapid (10+0)
2. Classical (30+0)

Enter 1 or 2:
```

That should be pretty self-explanatory, you basically choose between Rapid and Classical (the Lichess API doens't suppot anything else) by entering either 1 or 2. The timing of the games is also listed there; Rapid is 10min and Classical 30min (without extra-time, I might add support for extra-time later)

When you have input either 1 or 2, the program will start to search after an opponent. It shouldn't take long and the game should start pretty quickly.

```
Searching after opponent...
An opponent was found!
```


## How to contribute?
### TODO and Current Questions
* This program only works on Windows at the moment, can anyone make the Linux and macOS equivalent of the batch-file found in the `batch` folder?
* The chessboard that is displayed isn't very nice looking (it's just letters and dots!), but I'm unsure whether CMD allows much better graphics. The goal would be to create something like [this](https://www.reddit.com/r/chess/comments/cm394n/play_chess_against_stockfish_in_your_terminal/) on other systems like Linux for example.
* Make it so that the user can see the chat, maybe in an another terminal window. My plan was to create a second command (e.g. "lichess chat) so that you can open a second terminal window and type the command and then get the chat displayed.
* Add suppot for ranked games
* How do you change the POV (Point Of View) of the chessboard in python-chess? Is it even possible? The current program displays everything from the white's side so if you're black it might be a little weird.

### Useful links 
* https://lichess.org/api - Lichess API
* https://lichess.org/api#operation/apiBoardSeek - Create a "seek", match vs random player, lichess API
* https://berserk.readthedocs.io/en/master/installation.html - Python client for the Lichess API
* https://lichess.org/api#tag/Board - Lichess Board API
* https://chess.stackexchange.com/questions/28870/render-a-chessboard-from-a-pgn-file - How to save the python-chess board as an SVG-image