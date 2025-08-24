import pytest
from linear_board import *
from settings import *



def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.full() == False
    #assert empty.is_victory("x") == False


def test_add():
    b = LinearBoard()
    for i in range(board_leng):
        b.add("x")
    assert b.full() == True
"""
Test de Victory sin importar el jugador

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x")

    assert b.victory() == True
"""
def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x")
    assert b.victory("x") == True
    assert b.victory("o") == False      


def test_draw():
    b = LinearBoard()
    
    b.add ("o")
    b.add ("o")
    b.add ("x")
    b.add ("o")

    assert b.is_draw()    

def test_add_to_full():
    full = LinearBoard()
    for i in range(board_leng):
        full.add("x")

    full.add("x")
    assert full.full()

