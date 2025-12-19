class Noued: 
    def __init__(self, info) 
        self.info= info #information du noued
        self.fils= []   #listes des fils 
        self.pere= None #pointeur vers le pere papa 


def constArbreA(): 
    r = Noued("R") 
    a = Noued("A") 
    b = Noued("B") 
    c = Noued("C") 
    d = Noued("D") 

    r.fils = [a,b]
    a.pere = r 
    b.pere = r  
    
    a.fils = [c,d]
    c.pere= a 
    d.pere= a 

    return r 