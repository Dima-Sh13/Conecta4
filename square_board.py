from linear_board import LinearBoard
from settings import *
from list_utils import find_streak


class SqueareBoard():
    """
    Representa un tablero cuadrado de 4 LinearBoard.
    """
    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una lista de LinearBoard.
        """
        board = cls()
        board.board = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    def __init__(self):
        self.board = [LinearBoard() for i in range(board_leng)]
        

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
        vic = False
        return self.v_victory(char) or self.h_victory(char)
              
            
    def v_victory(self,char):
        result = False
        for list in self.board:
            result = list.victory(char)
            if result == True:
                break

        return result    

    def h_victory(self,char):
        result = False
        matrix = self.convert_to_matrix(self.board)
        for i in matrix:
            g = LinearBoard.fromList(i)
            print(g)
            result = g.victory(char)

            if result == True:
                break

        return result    


    def r_victory(self,char):
      def r_victory(self,char):
        vic= False
        strike = 1
        index = 0
        index2 = 0
        for i in self.board:
            lis = i.column
            index = 0
            for x in lis:
                if x == char:
                    
                    if index == index2 +1:
                        index2 = lis.index(char)
                        strike += 1
                        if strike == VICTORY_STRIKE:
                            vic = True
                
                index +=1
        return vic        
                
    def s_victory(self,char):
        return False
    def convert_to_matrix(self, matrix):
        new_matrix=[[],[],[],[]]
        index = 0
        index2 = 0
        for i in new_matrix:
            for x in matrix:
                i.append(x.column[index])
            index += 1
        return new_matrix         
    #dunders
    def __repr__(self):
        return f"{self.__class__}:{self.board}"













board = SqueareBoard()


