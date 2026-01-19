import time 
from collections import deque



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


def ConstruireArbreAutomatique(nb_noeuds, n=4):
    racine = Noeud("R")
    file = deque([racine])
    compteur = 1

    while compteur < nb_noeuds:
        courant = file.popleft()

        for i in range(n):
            if compteur >= nb_noeuds:
                break

            nouveau = Noeud(f"N{compteur}")
            nouveau.pere = courant
            courant.fils.append(nouveau)

            file.append(nouveau)
            compteur += 1

    return racine




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

def SupprimNoeud(racine, info):
    noeud = RechercheNoeud(racine, info)

    if noeud is None:
        print("Noeud non trouvé")
        return

    if noeud.pere is None:
        print("Impossible de supprimer la racine")
        return

    pere = noeud.pere

    # rattacher les fils du noeud à son père
    for f in noeud.fils:
        f.pere = pere
        pere.fils.append(f)

    # supprimer le noeud de la liste des fils du père
    pere.fils.remove(noeud)

    print(f"Noeud '{info}' supprimé (fils réattachés au parent)")


""" test 4 

if __name__ == ("__main__"):  
    racine = constArbreA() 

    print("Arbre initial:")  
    AfficherProfondeur(racine) 

    ModifyNoeud(racine, "X","M")
    print("\n Aprés la  Mofification: ") 
    AfficherProfondeur(racine) 

    SupprimNoeud(racine, "D" )

    print("\n Aprés la suppression:")
    AfficherProfondeur(racine) 
    
"""    

# function Affichege d'un sous arbre 

def AfficcherSousArbre(racine,info): 
    noeud = RechercheNoeud(racine, info) 

    if noeud is None: 
        print("Noeud non trouvé") 
        return 
    
    print( f"Sous arbre a partir de '{info}': ")
    AfficherProfondeur(noeud) 


#  function Vérifier si un Arbre estt complet

def IsArbreComplet(racine, n=4):
    if racine is None:
        return True

    file = deque([racine])
    fin = False  # indique qu'on a rencontré un noeud incomplet

    while file:
        noeud = file.popleft()

        # si un noeud incomplet a déjà été rencontré,
        # aucun noeud suivant ne doit avoir des fils
        if fin and noeud.fils:
            return False

        # si le noeud n'a pas exactement n fils,
        # alors les noeuds suivants doivent être des feuilles
        if len(noeud.fils) < n:
            fin = True

        for f in noeud.fils:
            file.append(f)

    return True




# function qui trouve le plus grand sous arbre complet 
#on doit d'abord trouver la taille de larbre 
#  
def TailleArbre(noeud): 
    if noeud is None: 
        return 0  
    return 1 + sum(TailleArbre(f) for f in noeud.fils)

def PGdArbreComplet(racine, n=4):
    best = None
    max_size = 0

    def parcourir(noeud):
        nonlocal best, max_size
        if noeud is None:
            return True, 0  # (est_complet, taille)

        taille = 1
        complet = True

        # tous les fils doivent être complets
        for f in noeud.fils:
            c, t = parcourir(f)
            if not c:
                complet = False
            taille += t

        # vérifier la condition de complétude locale
        if complet:
            if not IsArbreComplet(noeud, n):
                complet = False

        if complet and taille > max_size:
            max_size = taille
            best = noeud

        return complet, taille

    parcourir(racine)
    return best



""" test 5 

if __name__ == ("__main__"): 
    racine = constArbreA() 



    AfficcherSousArbre(racine, "A") 

    print("\n Arbre Complet ou non  :  ", IsArbreComplet(racine)) 

    sos = PGdArbreComplet(racine) 
if sos : 
    print ("\n Plus grand sous arbre complet : ")
    AfficherProfondeur(sos)
"""


# fonction qui tronsforme un arbre general en  arbre binaire  
# on deefinit un new type of noeud 

class Noeudbinaire: 
    def __init__(self, info): 
        self.info = info 
        self.gauche = None 
        self.droit = None 


def TransformEnBinaire(noeud): 
    if noeud is None: 
        return None
    
    binaire = Noeudbinaire(noeud.info)  

    if noeud.fils: 
        binaire.gauche = TransformEnBinaire(noeud.fils[0]) 

        courant = binaire.gauche 
        for f in noeud.fils[1:]: 
            courant.droit = TransformEnBinaire(f) 
            courant = courant.droit 

    return binaire 



# function pour l affichage de un arbr binaire 

def AffichageBinaire(noeud, niveau=0): 
    if noeud is None: 
        return 

    print("  " * niveau + str(noeud.info))
    AffichageBinaire(noeud.gauche, niveau + 1) 
    AffichageBinaire(noeud.droit, niveau + 1)  



"""test 6 

if __name__ == ("__main__"): 
    racine = constArbreA() 

    print("Arbre initial:")  
    AfficherProfondeur(racine) 

    binaire = TransformEnBinaire(racine) 
    print("\nArbre binaire transformé:") 
    AffichageBinaire(binaire)  
"""


#chemin entre 2 noeud 


def CheminRacine(noeud):
    chemin = []
    while noeud:
        chemin.append(noeud)
        noeud = noeud.pere
    return chemin[::-1]  # racine → noeud


def CheminEntreDeuxNoeuds(racine, info_a, info_b):
    a = RechercheNoeud(racine, info_a)
    b = RechercheNoeud(racine, info_b)

    if a is None or b is None:
        print("Un des noeuds n'existe pas")
        return

    chemin_a = CheminRacine(a)
    chemin_b = CheminRacine(b)

    i = 0
    while i < min(len(chemin_a), len(chemin_b)) and chemin_a[i] == chemin_b[i]:
        i += 1

    # chemin a → ancêtre commun → b
    chemin_final = chemin_a[i-1:][::-1] + chemin_b[i:]

    print("Chemin de", info_a, "vers", info_b, ":")
    print(" -> ".join(n.info for n in chemin_final))


# extracct dun sous arbre 


def CopierSousArbre(noeud):
    if noeud is None:
        return None

    nouveau = Noeud(noeud.info)
    for f in noeud.fils:
        fils_copie = CopierSousArbre(f)
        fils_copie.pere = nouveau
        nouveau.fils.append(fils_copie)

    return nouveau


def ExtraireSousArbre(racine, info):
    noeud = RechercheNoeud(racine, info)
    if noeud is None:
        print("Noeud non trouvé")
        return None

    return CopierSousArbre(noeud)


def EvaluationExperimentale():
    tailles = [10, 20, 30, 40, 50, 100]

    print("\n====== ÉVALUATION EXPÉRIMENTALE ======")
    print(f"{'Nb noeuds':<12} | {'Arbre complet (s)':<20} | {'Sous-arbre complet max (s)'}")
    print("-" * 60)

    for n in tailles:
        arbre = ConstruireArbreAutomatique(n)

        # Temps IsArbreComplet
        debut = time.time()
        IsArbreComplet(arbre)
        t1 = time.time() - debut

        # Temps PGdArbreComplet
        debut = time.time()
        PGdArbreComplet(arbre)
        t2 = time.time() - debut

        print(f"{n:<12} | {t1:<20.6f} | {t2:.6f}")



# Menu de l'application 

def Menu():
    racine = constArbreA()

    while True:
        print("\n====== MENU ======")
        print("1. Afficher l'arbre (profondeur)")
        print("2. Afficher l'arbre (largeur)")
        print("3. Insérer un noeud")
        print("4. Modifier un noeud")
        print("5. Supprimer un noeud")
        print("6. Afficher un sous-arbre")
        print("7. Hauteur de l'arbre")
        print("8. Vérifier si l'arbre est complet")
        print("9. Transformer en arbre binaire")
        print("10. Chemin entre deux noeuds")
        print("11. Extraire un sous-arbre")
        print("12. Évaluation expérimentale (complexité)")
        print("0. Quitter")

        choix = input("Votre choix : ")
        debut = time.time()

        if choix == "1":
            AfficherProfondeur(racine)

        elif choix == "2":
            AfficherLargeur(racine)

        elif choix == "3":
            p = input("Parent : ")
            n = input("Nouveau noeud : ")
            Insertnoeud(racine, p, n)

        elif choix == "4":
            a = input("Ancienne info : ")
            n = input("Nouvelle info : ")
            ModifyNoeud(racine, a, n)

        elif choix == "5":
            x = input("Noeud à supprimer : ")
            SupprimNoeud(racine, x)

        elif choix == "6":
            x = input("Racine du sous-arbre : ")
            AfficcherSousArbre(racine, x)

        elif choix == "7":
            print("Hauteur =", CalculeHauteur(racine))

        elif choix == "8":
            print("Arbre complet ?", IsArbreComplet(racine))

        elif choix == "9":
            binaire = TransformEnBinaire(racine)
            print("Arbre binaire :")
            AffichageBinaire(binaire)
        elif choix == "10":
            a = input("Noeud A : ")
            b = input("Noeud B : ")
            CheminEntreDeuxNoeuds(racine, a, b)

        elif choix == "11":
            x = input("Racine du sous-arbre : ")
            sous = ExtraireSousArbre(racine, x)
            if sous:
                print("Sous-arbre extrait :")
                AfficherProfondeur(sous)
        
        elif choix == "12":
            EvaluationExperimentale()


        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide")

        fin = time.time()
        print(f" Temps d'exécution : {fin - debut:.6f} secondes")


if __name__ == "__main__":
    Menu()


    
