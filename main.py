# from donnees import *
from utils import *
from src.jeu import Jeu
from src.joueur import Joueur

# cartes à check : 34, 39, 46, 51, 58, 70, 94, 96, 154

# valeur_de_base : 41, 60, 85, 102
# savoir si ca augmente apres utilisation ou seulement apres avoir attaqué
# donc ne s'applique pas si l'attaque miss


# effet à check dans le cas ou l'attaque/effet miss :
# disparition/provocation/temporatite/eternite/etourdissement


# à modifier dans effet.py tous les appel '().executer' -> en faire une sous-classe

# check effet dans le cas ou revanche (carte est morte) les passifs doivnet s'appliquer 

import msvcrt

if __name__ == '__main__': 

    N = 2
    n = 1

    def cartes_joueur(cartes, N=4, n=0):

        liste = random.sample(cartes, N)
        
        if  0 < n <= N:
            liste = random.sample(cartes[:-n], N-n)
            for i in range(1, n+1):
                liste.append(cartes[-i])

        return liste[::-1]
    
    print("")
    attaques = charger_attaques()
    cartes = charger_cartes()
    cartes_J1 = cartes_joueur(copy.deepcopy(cartes), N=N, n=n)
    cartes_J2 = cartes_joueur(copy.deepcopy(cartes), N=N, n=0)

    numero = 0
    for carte in copy.deepcopy(cartes):
        if numero <= 0:
            break
        if carte.numero == numero:
            cartes_J1[-1] = carte
            break

    J1 = Joueur(nom="Joueur 1", cartes=cartes_J1) 
    J2 = Joueur(nom="Joueur 2", cartes=cartes_J2)

    # J2.cartes[0].pv = 40

    jeu = Jeu(joueur1=J1, joueur2=J2)

    J1.elements = {Element.FEU : 9, Element.NATURE: 8, Element.EAU : 7, Element.TERRE: 6, Element.LUMIERE: 10, Element.OMBRE: 5}

    print("Appuyez sur une touche pour jouer...")
    msvcrt.getch()
    jeu.jouer()








