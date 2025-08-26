from linear_board import LinearBoard
from settings import *
from list_utils import find_streak


class SqueareBoard():
    """
    Representa un tablero cuadrado de 4 LinearBoard.
    """
    def __init__(self):
        self.board = [LinearBoard() for i in range(board_leng)]
        self.index = 0

    def full(self):
        """
        True si todas los LinearBoard estan llenos.
        """
        #Mi version
        is_full = True
        for list in self.board:
            for element in list:
                if element == None:
                    is_full = False
                    break
                    
        return is_full                
                
        """
        Version curso:
        (mas elegante que la mia)
        result = True
        for lb in self.board:
            result = result and lb.full()
        return result    
        """
            
    def victory(self,char):
        #return self.h_victory or self.v_victory or 
        pass      
            
    def v_victory(self,char):
        result = False
        for list in self.board:
            result = list.victory(char)
            if result == True:
                break

        return result    

    def h_victory(self,char):
        return False

    def r_victory(self,char):
        return False
    def s_victory(self,char):
        return False

board = SqueareBoard()


