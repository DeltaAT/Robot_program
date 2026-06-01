from automatas.tm import move_robot
from automatas.dfa import check_robot
import pytest

# Tests für die Turing Maschine
@pytest.mark.parametrize("robot", [
    "111#FFR",
    "11#FFR",
    "111#RRLL",
    "111#FFF",
    "111111111#FFFLRFFFLRLRLFFF"
])
def test_tm_true(robot):
    assert check_robot(robot) == True
    assert move_robot(robot) == True

@pytest.mark.parametrize("robot", [
    "1#FFR",
    "11#FFF",
    "1#FRRLLLLRLRLF",
    "11#LRLFLLFLF",
    "11111#FFLRFFLRFFLRF"
])
def test_tm_false(robot):
    assert check_robot(robot) == True
    assert move_robot(robot) == False