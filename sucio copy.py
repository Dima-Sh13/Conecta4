from settings import *

class LinearBoard():
    """
    Clase que representa una sola columna del tablero.
    Donde X es un jugador y O el otro.
    None representa que una posicion esta vacia.
    """
    @classmethod
    def fromList(cls,list):

        board = cls()
        board.column = list
        return board
    def __init__(self):
       self.column = [None for i in range(board_leng)]
       
    def add(self,char):
        "Juega en la primer posicion disponible"
        #buscamos la primera posicion libre"
        i = self.column.index(None)
        #lo sustituimos por char
        self.column[i]=char

        pass   

    def is_full(self):
        pass


    """
    def victory(self, char):
        strike = 0
        for i in self.column.column:
            if i == char:
                strike += 1
                if strike == VICTORY_STRIKE:
                    return True
            else:
                strike = 0
                         
        return False
       
    """
    
    def is_tie(self,char1,char2):
        pass


    def victory(self, char):
            strike = 1
            for i in self.column:
                if i == char:
                    strike += 1
                    if strike == VICTORY_STRIKE:
                        return True
                else:
                    strike = 1
            return False

def find_one(list, needle):
    if needle in list:
        return True
    

"""
def add(self, ficha):
        self.resultresult = ""
        memory = None
        counter = 0
        if ficha != "x" and ficha != "o":
            self.result = "Insert a valid ficha"
        else: 
            self.result = ficha 

        for i in BOARD:
            counter += 1
            
            if BOARD[i] != None:
                BOARD[memory] = self.result
            if counter == len(BOARD) and BOARD[i] == None:
                 BOARD[i] = self.result  


def victory(self):
        win_strike_x = 0
        win_strike_o = 0 
        for i in BOARD:
            if BOARD[i]== "x":
                win_strike_x +=1
                win_strike_o = 0
            elif BOARD[i] == "o":
                win_strike_o += 1
                win_strike_x = 0

        if win_strike_x == VICTORY_STRIKE or win_strike_o == VICTORY_STRIKE:
            return True                  


    if None in self.column:#buscamos la primera posicion libre"           

    self.is_full = False             


    def victory(self):
        x_win= 0
        o_win = 0
        for i in self.column:
            if i == "x":
                x_win +=1
                o_win = 0
            elif i== "o":
                o_win +=1
                x_win = 0

        if x_win == VICTORY_STRIKE or o_win == VICTORY_STRIKE:

            return True            


     def is_draw(self):
        x_win= 0
        o_win = 0
        for i in self.column:
            if i == "x":
                x_win +=1
                o_win = 0
            elif i== "o":
                o_win +=1
                x_win = 0

        if x_win == VICTORY_STRIKE or o_win == VICTORY_STRIKE:

            return False    
        else:
            return True                     
"""



class SqueareBoard():
    
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
    def convert_to_matrix(self, matrix):
        new_matrix=[[],[],[],[]]
        index = 0
        index2 = 0
        for i in new_matrix:
            for x in matrix:
                i.append(x.column[index])
            index += 1
        return new_matrix      
                
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
        
    
                        
                    

                        
                        
                
                    
          
        """
        for key, values in dic.items():
            for i in values[1:]:
               if i == w_pos + 1 or i == w_pos - 1:
                   w_pos = i
                   strike +=1
                   if strike == VICTORY_STRIKE:
                       vic = True
                       break 
                       
        
        r_strike = 1
        s_strike = 1
        val = []
        char1 = 
        for values in dic.values():
            val.append(values)
            for x in val:
                for i in x:


                
        return vic                        

        """

            
        
            
        
                
           

board2 = SqueareBoard()
diagonal_victory = SqueareBoard.fromList([["x",None,None,None],
                                             ["o","x",None,None],
                                             ["x","o","x",None],
                                             ["x","o",None,"x"]])

print(diagonal_victory.r_victory("x"))
