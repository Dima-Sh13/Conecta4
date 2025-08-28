import pytest
from square_board import *
from linear_board import *

def square_board():
    b = SqueareBoard()
    assert b.full() == False
    assert b.victory("o") == False
    assert b == True
    assert b.victory("x") == False

def test_v_victory():
    vertical = SqueareBoard.fromList([["o","x","x","x"],
                                      [None,None,None,None],
                                      [None,None,None,None],
                                      [None,None,None,None]])
    pass

def test_h_victory():
    horizontal_victory = SqueareBoard.fromList([["x",None,None,None],
                                             ["x","o",None,None],
                                             ["x","o",None,None],
                                             ["x","o",None,None]])
    assert horizontal_victory.h_victory("x") == True

def test_add():
    pass


def test_detect_victory():
    pass

def test_detect_tie():
    pass


def test_detect_full():
    pass