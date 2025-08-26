import pytest
from square_board import *
from linear_board import *

def square_board_test():
    b = SqueareBoard()
    assert b.full() == False
    assert b.victory("o") == False
    assert b == True
    assert b.victory("x") == False

def v_victory_test():
    vertical = SqueareBoard.fromList([["o","x","x","x"],
                                      [None,None,None,None],
                                      [None,None,None,None],
                                      [None,None,None,None]])
    pass


def test_add():
    pass


def test_detect_victory():
    pass

def test_detect_tie():
    pass


def test_detect_full():
    pass