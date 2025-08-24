import pytest
from list_utils import *
from settings import *


def test_find_one():
    needle = 1
    none = [0,0,5,"s"]
    beginning =[1,None,9,6,0,0]
    end = ["x", "0", 1]
    several = [0,0,3,4,1,3,2,1,3,4]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(end,needle)
    assert find_one(several,needle)

def test_find_n():
    needle = 1
    none = [0,0,5,"s"]
    beginning =[1,None,9,6,0,0]
    end = ["x", "0", 1]
    several = [0,0,3,4,1,3,2,1,3,4]

    assert find_n (none, needle) == False
    assert find_n (beginning, needle) == 1
    assert find_n (end, needle) == 1
    assert find_n (several, needle) == 2

def test_find_streak():
    needle = 1
    several = [0,0,3,4,1,1,1,2,3,4]

    assert find_streak(several, needle) == True