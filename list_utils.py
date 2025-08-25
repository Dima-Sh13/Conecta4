from settings import *

def find_one(list, needle):
    #Devuelve True si encuentra al menos una ocurrencia de needle en List
    """
    Version Curso:
    def find_one(list,needle):

    found = False
    index = 0
    while not found and index < len(list):
        if needle == list[index]:
            found = True
            break
        index += 1

    return found        
    
    #Mi version
    pos = []
    if needle in list:
        pos.append(list[needle])
        return True
    else:
        return False
    """
    return find_n(list, needle, 1)


def find_n(list,needle, n):
    """
    Devuelve True si la lista tienen las mismas instancias de needle que n.
    """
    result = False
    rep = 0
    index = 0
    while index < len(list):
        if needle == list[index]:
            rep += 1    
        
        index += 1
    if rep >= n and n >= 0:
        result = True

    return result    

def find_streak(list,needle, n):
    """
    Encuentra si hay un streak de 3 ganador.
    """
    mem = ""
    streak = 1
    index = 0
    while index < len(list):
        if needle == list[index] and  needle == mem:
            streak += 1 
            if streak == n:
                return True 
        else :
            streak = 1      
        mem = list[index]
        index += 1
        
    return False
  
