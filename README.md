<!--![Terminal Lichess](docs/images/lichess.png)-->

<h1 align="center">
  <img height="200" src="docs/images/logo.png">
  <br>
  Lichs (Lichess in the Terminal)
</h1>

<p align="center">
  <a href="https://github.com/Cqsi/lichs">
    <img src="https://img.shields.io/badge/project-semi--active-orange" alt="project-active" />
  </a>
  <a href="https://github.com/Cqsi/lichs">
    <img src="https://img.shields.io/badge/Contributions-welcome-brightgreen" alt="contributions-welcome" />
  </a>
  <a href="https://github.com/Cqsi/lichs/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license-mit" />
  </a>
  <a href="https://pypi.org/project/lichs/">
    <img src="https://img.shields.io/pypi/v/lichs" alt="pypi-version" />
  </a>
</p>

## Info and requirements
* <ins>Uses Lichess</ins>, which means that you need to have a Lichess account
* Only Classical and Rapid games because the Lichess API doesn't allow anything else (quite frankly, Blitz and Bullet like games wouldn't be a lot of fun since you would have to input the coordinates really fast)
* This program uses [SAN](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))-notation, see the [Important](#Important)-section.

Lichs uses the Lichess API (more exactly [berserk](https://github.com/rhgrant10/berserk)) to make it possible for you to play against other real players directly in the terminal on Lichess servers. <ins>This project is still in its early stages; there's no chat support, pretty bad graphics, no ranked games and probably some bugs.</ins>

If like this project, be sure to also check out [Nick Zuber's Chs-project](https://github.com/nickzuber/chs), since it was his project that inspired me to do this in the first place.


## Installation

This package is available on [PyPi](https://pypi.org/project/lichs/), therefore just run:

```
$ pip install lichs
```
and the program will be installed. The next step is to generate a personal API-key.

### How to generate a personal API token

1. [Create a Lichess API token](https://lichess.org/account/oauth/token/create?scopes[]=board:play&description=Lichs+cli+play), log into Lichess if necessary
2. Click the button `Submit` in the lower right corner
3. Copy the token shown in the brown box
4. Jump into your terminal and write `lichs <api_token>` (put your API token instead of `<api_token>`) and run the command. To get this clear, an example would have been `lichs lzRceo5XOUND74Lm`. You should then see a message to confirm that the API token has been saved. 


## Usage

You start playing by typing the command `lichs` into your terminal:

```
$ lichs
```

That will take you to the intro screen:

```
Welcome to Lichess!

What kind of chess do you want to play?
1. Rapid (10+0)
2. Classical (30+0)

Enter 1 or 2:
```

That should be pretty self-explanatory, you basically choose between Rapid and Classical (the Lichess API doens't support anything else) by entering either 1 or 2. The timing of the games is also listed there; Rapid is 10min and Classical 30min (without extra-time, I might add support for extra-time later)

When you have input either 1 or 2, the program will start to search after an opponent. It shouldn't take long and the game should start pretty quickly.

```
Searching after opponent...
An opponent was found!
```

Then the program will let you know whether you're the color white or black. After that you will start playing; the program will output the board after every move and ask for your move when it's your turn.

```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . P . . .
P P P P . P P P
R N B Q K B N R
```
Above is an example of the board displayed. <ins>Note:</ins> at the moment the board is always displayed from the white's side, because I don't know how to fix this.


### Important
When the program asks for your move, you need to input the move in [standard algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) (SAN). Basically, it specifies <ins>which piece</ins> to move and <ins>to where</ins>. As an example, to move a knight from g1 to f3, you type in **Nf3** (N is for Knight, since Rook uses K). If you want to learn more, click on the link above.

The program will inform you if you can't make the move you have input.

Support for UCI-notation might get added later.

## Contributions

<a href="https://github.com/Cqsi/lichs/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Cqsi/lichs" />
</a>

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for how to contribute.
