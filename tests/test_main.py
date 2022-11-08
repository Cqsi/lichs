import pytest
import io

from lichs.__main__ import get_game_type_input


@pytest.mark.parametrize('user_input,exp_time,exp_inc', [('1', 10, 0),
                                                              ('2', 30, 0),
                                                              ('3\n15 15', 15, 15),
                                                              ('kjshfkjsdf\n1', 10, 0)])
def test_get_game_type_input(monkeypatch, user_input, exp_time, exp_inc):
    """Tests the different kinds of input that might be given while setting up a game."""
    monkeypatch.setattr('sys.stdin', io.StringIO(user_input))
    time, inc = get_game_type_input()
    assert time == exp_time
    assert inc == exp_inc
