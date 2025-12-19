class Noeud: 
    def __init__(self, info) 
        self.info= info #information du noued
        self.fils= []   #listes des fils 
        self.pere= None #pointeur vers le pere papa 

#construction d'un arbre exemple 

def constArbreA(): 
    r = Noeud("R") 
    a = Noeud("A") 
    b = Noeud("B") 
    c = Noeud("C") 
    d = Noeud("D") 

    r.fils = [a,b]
    a.pere = r 
    b.pere = r  
    
    a.fils = [c,d]
    c.pere= a 
    d.pere= a 

    return r 


#affichage d'arbre en parcour profondeur 

def AfficherProfondeur(Noeud, niveau=0):
    if Noeud is None: 
        return 
    print(" " * niveau * 2 + Noeud.info) 
    for f in Noeud.fils : 
        AfficherProfondeur(f, niveau+1) 