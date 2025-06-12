from utils import *
from src.effet import GestionEvenement

if TYPE_CHECKING:
    from joueur import Joueur
    from carte import Carte
    from attaque import Attaque

class Jeu:
    def __init__(self,
                 joueur1: "Joueur",
                 joueur2: "Joueur"):

        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur1.adversaire = joueur2
        self.joueur2.adversaire = joueur1
        self.joueurs = [self.joueur1, self.joueur2]
        self.premier_joueur = None
        self.tour = 1
        self.tour_complet = self.tour
        self.terrain = None
        self.gestion_evt = GestionEvenement()
        for joueur in self.joueurs:
            joueur.jeu = self
                
    def initialisation_passifs(self) -> None:
        self.gestion_evt.initialisation_passifs_evt()
        for joueur in self.joueurs:
            for carte in joueur.cartes:
                for passif in carte.passifs:
                    if isinstance(passif.evenement, list):
                        for evenement in passif.evenement:
                            self.gestion_evt.enregistrer(evenement, passif)
                    else:
                        self.gestion_evt.enregistrer(passif.evenement, passif)

    def mise_a_jour_statut(self) -> None:
        for joueur in self.joueurs:
            for carte in joueur.liste_cartes_vivantes():
                carte.mise_a_jour_statut()

    def test_cible_valide(self, attaque: "Attaque", carte_cible: "Carte") -> bool:
        
        joueur = attaque.carte.joueur
        adversaire = joueur.adversaire
        
        test_provocation = any(any(effet.nom == "PROVOCATION" for effet in c.statut) for c in adversaire.liste_cartes_vivantes())

        if carte_cible.joueur != joueur and any(effet.cible == TypeCible.UNE_CARTE_ALLIEE for effet in attaque.effets):
            print("❌ La carte ciblée doit être une carte alliée")
            return False

        if carte_cible.joueur != adversaire and any(effet.cible == TypeCible.UNE_CARTE_ENNEMIE for effet in attaque.effets):
            print("❌ La carte ciblée doit être une carte ennemie")
            return False
        
        if test_provocation and carte_cible.joueur == adversaire and not any(effet.nom == "PROVOCATION" for effet in carte_cible.statut):
            print("❌ La carte ciblée doit être une carte sous PROVOCATION")
            return False
        
        return True

    def appliquer_terrain(self, valeur: int, element: Element) -> None:
        self.terrain = (element, valeur)
        print(f"🔷 Le terrain devient {element.name}")
    
    def liste_cartes_mortes(self) -> List["Carte"]:
        return self.joueur1.liste_cartes_mortes() + self.joueur2.liste_cartes_mortes()
    
    def liste_cartes_mortes_string(self) -> List[str]:
        return self.joueur1.liste_cartes_mortes_string() + self.joueur2.liste_cartes_mortes_string()

    def liste_cartes_vivantes(self) -> List["Carte"]:
        return self.joueur1.liste_cartes_vivantes() + self.joueur2.liste_cartes_vivantes()
    
    def liste_cartes_vivantes_string(self) -> List[str]:
        return self.joueur1.liste_cartes_vivantes_string() + self.joueur2.liste_cartes_vivantes_string()

    def demander_choix(self, 
                       choix_possibles_string: List[str], 
                       choix_possibles: Optional[List[Any]] = None, 
                       message: str = "", 
                       defaut: str = "") -> Any:
        
        print("\n" + message)

        if choix_possibles is None: 
            choix_possibles = choix_possibles_string.copy()

        liste_string = choix_possibles_string.copy()
        liste = choix_possibles.copy()
        if defaut:
            liste_string.insert(0, defaut)
            liste.insert(0, defaut)

        for i, element in enumerate(liste_string):
            print(f" {i}. {element}")

        choix = input("👉 Choisis un numéro : ")

        while '²' in choix  or not choix.isdigit() or not (0 <= int(choix) <= len(liste_string) - 1):
            choix = input("❌ Choix invalide. Rechoisis : ")


        index = int(choix)
        print(f"✅ Tu as choisi : {liste_string[index]}\n")

        return liste[index]

    def selectionner_carte(self, joueur: "Joueur", defaut: str = "Retour") -> Union["Carte", str]:
        cartes = joueur.liste_cartes_vivantes()
        cartes_str = joueur.liste_cartes_vivantes_string()

        carte_choisie = self.demander_choix(choix_possibles_string=cartes_str,
                                            choix_possibles=cartes,
                                            message="Choisis une carte : ", 
                                            defaut=defaut)
        return carte_choisie
    
    def selectionner_attaque(self, carte: "Carte", defaut: str = "Retour") -> Union["Attaque", str]:
        attaques = carte.liste_attaques_dispo()

        if any(effet.nom == "ETOURDISSEMENT" for effet in carte.statut):
            print(f"❌ {carte.nom} est étourdie ce tour")
            return defaut

        if not attaques:
            print("❌ Aucune attaque disponible pour cette carte ce tour")
            return defaut        

        attaques_str = carte.liste_attaques_dispo_string()

        attaque_choisie = self.demander_choix(choix_possibles_string=attaques_str,
                                              choix_possibles=attaques,
                                              message="Choisis une attaque : ",
                                              defaut=defaut)
        
        if attaque_choisie != defaut:
            self.gestion_evt.declencher(TypeEvenement.CHOIX_ATTAQUE, attaque=attaque_choisie)

        if attaque_choisie != defaut and not attaque_choisie.valide:
            attaque_choisie.valide = True
            return defaut
        
        if attaque_choisie != defaut and attaque_choisie.test_attaque_a_choix():
            return self.selectionner_choix(attaque_choisie, defaut=defaut)

        return attaque_choisie
    
    def selectionner_choix(self, attaque: "Attaque", defaut: str = "Retour") -> Union["Attaque", str]:

        attaques_choix_str = []
        attaques_choix = []

        for a in [atq for atq in attaque.effets_avec_choix if isinstance(atq, list)]:
            attaques_choix_str.append(" + ".join(e.nom for e in a))
            attaques_choix.append(a)

        attaque_choisie = self.demander_choix(choix_possibles_string=attaques_choix_str,
                                           choix_possibles=attaques_choix,
                                           message="C'est une attaque à choix, choisis une attaque : ",
                                           defaut=defaut)
        
        if attaque_choisie != defaut:

            for atq in attaques_choix:
                est_choisie = atq == attaque_choisie
                for effet in atq:
                    effet.choix = not est_choisie
                    effet.choisi = est_choisie

            attaque.cible_necessaire = any(effet.cible_necessaire for effet in attaque_choisie)

            return attaque

        return attaque_choisie

    def selectionner_cible(self, attaque: "Attaque", defaut: str = "Retour") -> Optional[Union["Carte", str]]:

        if not attaque.cible_necessaire:
            print("ℹ️  Pas besoin de cible pour cette attaque")
            return None

        cartes = self.liste_cartes_vivantes()
        cartes_str = self.liste_cartes_vivantes_string()
            
        for i, carte in enumerate(cartes):
            if carte.fumee and attaque.carte.joueur != carte.joueur:
                cartes_str[i] = carte_fumee
        
        cible_choisie = self.demander_choix(choix_possibles_string=cartes_str,
                                            choix_possibles=cartes,
                                            message="Choisis une cible : ",
                                            defaut=defaut)
        
        if cible_choisie != defaut and not self.test_cible_valide(attaque, cible_choisie):
            return defaut

        return cible_choisie 

    def tour_joueur(self, joueur_actif: "Joueur") -> bool:

        print(f"\n🕐 Tour {self.tour} : {joueur_actif.nom}")
        
        self.mise_a_jour_statut()
        self.gestion_evt.declencher(TypeEvenement.DEBUT_TOUR, joueur=joueur_actif)

        self.affichage_jeu(joueur_actif)

        action = ""
        action_fin = "Fin du tour"
        action_retour = "Retour"

        while action != action_fin:

            action = self.demander_choix(choix_possibles_string=["Utiliser une carte"],
                                         message="Choisis une action : ",
                                         defaut=action_fin)
            
            if action == action_fin:
                break
            
            carte_choisie = self.selectionner_carte(joueur_actif, defaut=action_retour)

            if carte_choisie == action_retour:
                self.affichage_jeu(joueur_actif)
                continue
            
            attaque_choisie = self.selectionner_attaque(carte_choisie, defaut=action_retour)

            if attaque_choisie == action_retour:
                self.affichage_jeu(joueur_actif)
                continue

            cible_choisie = self.selectionner_cible(attaque_choisie, defaut=action_retour)

            if cible_choisie == action_retour:
                self.affichage_jeu(joueur_actif)
                continue
            
            attaque_choisie.attaquer(cible_choisie)
            self.affichage_jeu(joueur_actif)

            if self.test_fin_jeu():
                return True

        joueur_actif.decrementer_recharge()
        
        if self.test_fin_jeu():
            return True

        return False

    def initialisation(self) -> None:

        # self.premier_joueur = random.choice(self.joueurs)
        self.premier_joueur = self.joueur1
        second_joueur = self.premier_joueur.adversaire

        print("")
        self.premier_joueur.decrementer_recharge(n=1)
        second_joueur.decrementer_recharge(n=2)
        print("")

        self.initialisation_passifs()

    def test_fin_jeu(self) -> bool:
        return not (self.joueur1.est_vivant() and self.joueur2.est_vivant())
    
    def boucle_jeu(self) -> None:

        joueur = self.premier_joueur
        self.tour_complet = 0

        while True:
            if self.tour_joueur(joueur):
                break
            joueur = joueur.adversaire
            self.tour_complet += 1
            if self.tour_complet % 2 == 0:
                self.tour += 1

    def jouer(self) -> None:    

        print(f"\n🎮 Début du jeu entre {self.joueur1.nom} et {self.joueur2.nom}")

        self.initialisation()

        self.gestion_evt.declencher(TypeEvenement.DEBUT_JEU)

        for joueur in self.joueurs:
            for carte in joueur.cartes:
                for attaque in carte.attaques:
                    if attaque.effets_passifs:
                        self.gestion_evt.declencher(TypeEvenement.DEBUT_JEU, attaque=attaque)

        self.boucle_jeu() 

        print(f"🎮 Fin du jeu entre {self.joueur1.nom} et {self.joueur2.nom}")
        if self.joueur1.est_vivant():
            print(f"🏆 Le gagnant est {self.joueur1.nom} !")
        else:
            print(f"🏆 Le gagnant est {self.joueur2.nom} !")

    def affichage_terrain(self):
        if self.terrain:
            print(f" Terrain | {self.terrain[0].name}: {self.terrain[1]}", end="")

    def affichage_jeu(self, joueur: "Joueur"):
        print("\n")
        self.joueur2.affichage_elements()
        print("\n")
        self.joueur2.affichage_cartes(joueur)

        print("----------------------------------------", end="")
        self.affichage_terrain()

        print("")
        self.joueur1.affichage_cartes(joueur)
        print("")
        self.joueur1.affichage_elements()
        print("\n")

