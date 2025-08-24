from settings import *


class LinearBoard():
    """
    Clase que representa una sola columna del tablero.
    Donde X es un jugador y O el otro.
    None representa que una posicion esta vacia.
    """
   
    def __init__(self):
        self.column =[None for i in range(board_leng)]
      

    def add(self, char):
        "Juega en la primer posicion disponible"
    
        if self.full() == False:
            i = self.column.index(None)
            self.column[i]=char  #lo sustituimos por char
      
      
    
    
    def full(self):
        """
        Mi version de full, se recorre la lista 
        y si no hay ningun None devuelve True
        """
        """
        isfull = 0
        for i in self.column:
            if i != None:
                isfull +=1
        if isfull == board_leng:
            return True        
        else:
            return False
        """
        return self.column[-1] != None        

    def victory(self, char):
        strike = 0
        for i in self.column:
            if i == char:
                strike += 1
                if strike == VICTORY_STRIKE:
                    return True
            else:
                strike = 0
        return False
   
    def is_draw(self):
       """
       No hay victoria ni de cchar "x" ni de char "o" 
       
       Version curso:
       return (self.victory("x") == False) and (self.victory("o") == False)
       
       """
       #Mi version 
       if not self.victory("x") or not self.victory("o"):
           return True
     
            

          
    
         



