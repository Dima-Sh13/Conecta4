from settings import *


class LinearBoard():
    """
    Clase que representa una sola columna del tablero.
    Donde X es un jugador y O el otro.
    None representa que una posicion esta vacia.
    """
   
    def __init__(self):
        self.column =[None for i in range(board_leng)]
        self.is_full = False

    def add(self, char):
        "Juega en la primer posicion disponible"
    
        if None in self.column:#buscamos la primera posicion libre"
            i = self.column.index(None)
        #lo sustituimos por char
            self.column[i]=char
        else:
            print(f"El tablero esta lleno")    
    
    
    def full(self):
        isfull = 0

        for i in self.column:
            if i != None:
                isfull +=1
        if isfull == board_leng:
            return True        
        else:
            return False
                

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
            
            

          
    
         



