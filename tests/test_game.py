import pytest
import chess
from lichs.Game import Game

@pytest.mark.parametrize('is_white,exp_board', [(
    True,
    '\x1b[40m\x1b[37m♖ \x1b[47m\x1b[30m♞ \x1b[40m\x1b[37m♗ \x1b[47m\x1b[30m♛ '
    '\x1b[40m\x1b[37m♔ \x1b[47m\x1b[30m♝ \x1b[40m\x1b[37m♘ \x1b[47m\x1b[30m♜ \x1b[40m\x1b[37m 8\n'
    '\x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ '
    '\x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[40m\x1b[37m 7\n'
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  '
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m 6\n'
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  '
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[40m\x1b[37m 5\n'
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  '
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m 4\n'
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  '
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[40m\x1b[37m 3\n'
    '\x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ '
    '\x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m 2\n'
    '\x1b[47m\x1b[30m♖ \x1b[40m\x1b[37m♞ \x1b[47m\x1b[30m♗ \x1b[40m\x1b[37m♛ '
    '\x1b[47m\x1b[30m♔ \x1b[40m\x1b[37m♝ \x1b[47m\x1b[30m♘ \x1b[40m\x1b[37m♜ \x1b[40m\x1b[37m 1\na b c d e f g h'
), (
    False,
    '\x1b[40m\x1b[37m♖ \x1b[47m\x1b[30m♞ \x1b[40m\x1b[37m♗ \x1b[47m\x1b[30m♛ '
    '\x1b[40m\x1b[37m♔ \x1b[47m\x1b[30m♝ \x1b[40m\x1b[37m♘ \x1b[47m\x1b[30m♜ \x1b[40m\x1b[37m 1\n'
    '\x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ '
    '\x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[47m\x1b[30m♟ \x1b[40m\x1b[37m♙ \x1b[40m\x1b[37m 2\n'
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  '
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m 3\n'
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  '
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[40m\x1b[37m 4\n'
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  '
    '\x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m 5\n'
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  '
    '\x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[47m\x1b[30m  \x1b[40m\x1b[37m  \x1b[40m\x1b[37m 6\n'
    '\x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ '
    '\x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m♟ \x1b[47m\x1b[30m♙ \x1b[40m\x1b[37m 7\n'
    '\x1b[47m\x1b[30m♖ \x1b[40m\x1b[37m♞ \x1b[47m\x1b[30m♗ \x1b[40m\x1b[37m♛ '
    '\x1b[47m\x1b[30m♔ \x1b[40m\x1b[37m♝ \x1b[47m\x1b[30m♘ \x1b[40m\x1b[37m♜ \x1b[40m\x1b[37m 8\nh g f e d c b a'
)])
def test_enhanced_display_transformation(is_white, exp_board):
    """Tests that the board is transformed properly"""
    berserk_board = str(chess.Board())
    Game.isWhite = is_white
    enhanced_board = Game.enhance_board_display(Game, berserk_board)
    assert exp_board == enhanced_board

