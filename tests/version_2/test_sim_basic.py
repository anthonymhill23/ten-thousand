import pytest
from tests.flo import diff
from ten_thousand.game import Game

pytestmark = [pytest.mark.version_2]

# @pytest.mark.skip("pending")
def test_quitter():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/quitter.sim.txt")
    assert not diffs, diffs

#@pytest.mark.skip("pending")
def test_one_and_done():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/one_and_done.sim.txt")
    assert not diffs, diffs

#@pytest.mark.skip("pending")
def test_single_bank():
    game = Game()
    try:
        diffs = diff(
            game.play, path="tests/version_2/bank_one_roll_then_quit.sim.txt"
        )
    except Exception as e:
        print(e)
    assert not diffs, diffs

@pytest.mark.skip("pending")
def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(
        game.play, path="tests/version_2/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs