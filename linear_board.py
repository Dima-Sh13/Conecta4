from settings import *


class LinearBoard():
    """
    Clase que representa una sola columna del tablero.
    Donde X es un jugador y O el otro.
    None representa que una posicion esta vacia.
    """
   
    def __init__(self, BOARD):
        self.pos1 = BOARD["pos1"]
        self.pos2 = BOARD["pos2"]
        self.pos3 = BOARD["pos3"]
        self.pos4 = BOARD["pos4"]
        self.is_full = False

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
    
    
    def full(self):
        if self.pos1 != None and self.pos2 != None and self.pos3 != None and self.pos4 != None:
            self.is_full = True
                

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
        

            
            

          
    
         



