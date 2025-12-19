from tkinter.filedialog import test


class Noeud: 
    def __init__(self, info):
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


"""test 
if __name__ == "__main__": 
    racine = constArbreA() 
    AfficherProfondeur(racine)
""" 


#function pour le parcour en largeur 

from collections import deque
def AfficherLargeur(racine): 
    if racine is None: 
        return

    file=deque([racine])

    while file:
        Noeud = file.popleft()
        print(Noeud.info, end=" ")

        for f in Noeud.fils:
            file.append(f)
    print ()


#calcule de la hauteur d'un arbre 

def CalculeHauteur(Noeud):
    if Noeud is None: 
        return -1 
    
    if not Noeud.fils: 
        return 0
    
    return 1 + max(CalculeHauteur(f) for f in Noeud.fils) 


#test2 

if __name__ == "__main__": 
    racine = constArbreA() 
    print("Affichage en profondeur : ")
    AfficherProfondeur(racine) 
    print("\n Affichage en Largeur :") 
    AfficherLargeur(racine) 
    print("\n la Hauteur de l'arbre est : ", CalculeHauteur(racine)) 

