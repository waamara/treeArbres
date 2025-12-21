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


"""test2 

if __name__ == "__main__": 
    racine = constArbreA() 
    print("Affichage en profondeur : ")
    AfficherProfondeur(racine) 
    print("\n Affichage en Largeur :") 
    AfficherLargeur(racine) 
    print("\n la Hauteur de l'arbre est : ", CalculeHauteur(racine)) 

""" 


# function qui recherhe un noeud dans l'arbre 

def RechercheNoeud (Noeud, info):  
    if Noeud is None:  
        return None 
    
    if Noeud.info == info: 
        return Noeud  
    
    for f in Noeud.fils: 
        res= RechercheNoeud(f,info)
        if res is not None: 
            return res 
        
    return None  


# funcction Inserer un noeud dans l'arbre 

def Insertnoeud (racine , info_parent , info_new):
    parent = RechercheNoeud(racine , info_parent)
    
    if parent is None: 
        print("Parent non trouvé") 
        return 
    
    if len(parent.fils) >=4: 
        print ("Le parent a déja 4 fils ")
        return 
    
    new = Noeud(info_new)
    new.pere = parent 
    parent.fils.append(new) 

    print(f" Noeud '{info_new}' inséré sous le parent '{info_parent}'")



""" test 3

if __name__ == "__main__": 
    racine = constArbreA() 

    print ("Arbre initial :" ) 
    AfficherProfondeur(racine) 

    Insertnoeud(racine , "B", "X" ) 
    print ("\n Arbre aprés insertion :") 

    AfficherProfondeur(racine) 
""" 

# funtion pour moddiifier un Noeud 

def ModifyNoeud (racine , anc_info , nov_info):
    noeud = RechercheNoeud(racine,anc_info)

    if noeud is None: 
        print("Noeud non trouvé") 
        return
    
    noeud.info=nov_info 
    print(f"Noeud '{anc_info}' modifié en '{nov_info}'" ) 


# Function qui Supprime un Noeud 

def SupprimNoeud(racine , info):
    noeud = RechercheNoeud(racine, info)

    if noeud is None: 
        print("Noeud non trouvé") 
        return 
    
    if noeud.pere is None: 
        print("Impossibl d supprimer la racin") 
        return 
    
    if noeud.fils: 
        print(" Impossible de supprimer ccar le Noeud a des fils  ") 
        return
    
    pere = noeud.pere 
    pere.fils.remove(noeud) 

    print (f" Noeud '{info}' supprimé") 

'''