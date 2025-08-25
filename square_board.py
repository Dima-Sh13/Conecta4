from linear_board import LinearBoard
from settings import *
from list_utils import find_streak


class SqueareBoard():
    def __init__(self):
        self.board = [None for i in range(board_leng)],[None for i in range(board_leng)],[None for i in range(board_leng)],[None for i in range(board_leng)]

    def add(self,char):
        index=0
        for i in self.board:
            for element in i:
                if i[index] == None:
                    i[index] = char
                    break
                else:
                    index +=1
            break    
            

board = SqueareBoard()
s

print(board.board)
board.add(x)
board.add(x)
board.add(x)
board.add(x)
board.add(x)
board.add(x)
print(board.board)    