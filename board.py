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
"""