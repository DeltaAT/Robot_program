from automatas.dfa import check_robot
import pytest

# Tests für den DFA
@pytest.mark.parametrize("robot", [
    "1#",
    "1#F",
    "111#FFR",
    "1111#RRLL",
    "11111#FFRFL"
])
def test_dfa_true(robot):
    assert check_robot(robot) == True

@pytest.mark.parametrize("robot", [
    "#",
    "#FFR",
    "111",
    "111FFR",
    "111#FX",
    "11##FF"
])
def test_dfa_false(robot):
    assert check_robot(robot) == False
