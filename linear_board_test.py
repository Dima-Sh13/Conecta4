import pytest
from linear_board import *
from settings import *



def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full == False
    #assert empty.is_victory("x") == False


def test_add():
    b = LinearBoard()
    for i in range(board_leng + 1):
        b.add("x")
    #assert b.is_full == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x")

    assert b.victory() == True
   


def test_draw():
    b = LinearBoard()
    
    b.add ("o")
    b.add ("o")
    b.add ("x")
    b.add ("o")

    assert b.is_draw()    

