from utils import *

from src.carte import Carte
from src.joueur import Joueur
from src.attaque import Attaque

class GestionEvenement:
    def __init__(self):
        self.initialisation_passifs_evt()

    def enregistrer(self, evenement: TypeEvenement, passif: "Effet") -> None:
        if evenement:
            self.passifs_evt[evenement].append(passif)

    def declencher(self, evenement: TypeEvenement, **donnees) -> None:
        attaque = donnees.get("attaque")
        donnees["evenement"] = evenement

        if evenement == TypeEvenement.CARTE_MORTE:
            carte, attaque = donnees.get("carte"), donnees.get("attaque")
            print(f"💀 {carte.nom} est tuée par {attaque.carte.nom}")
            carte.joueur.ajouter_carte_morte(carte)

        if attaque and hasattr(attaque, "effets_passifs_evt"):
            donnees["passif_attaque"] = True
            for passif in attaque.effets_passifs_evt[evenement]:
                passif.declencher(**donnees)
    
        donnees["passif_attaque"] = False
        for passif in self.passifs_evt[evenement]:
            passif.declencher(**donnees)

    def initialisation_passifs_evt(self):
        self.passifs_evt = {e: [] for e in TypeEvenement}

    def affichage_passifs_evt(self):
        for evenement, passifs in self.passifs_evt.items():
            if passifs:
                print(f"{evenement.name} :", end=" ")
                for passif in passifs:
                    print(passif.nom, end=" ")
                print("")

class Effet(ABC):
    def __init__(self, 
                 valeur: Union[int, List[int], float, List[float]] = 0, 
                 element: Optional[Element] = None, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 duree: int = 0,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE,
                 evenement: Optional[Union[TypeEvenement, List[TypeEvenement]]] = None,
                 symbole: str = ""):
        
        self.attaque = None
        self.element = element
        self.evenement = evenement
        self.element_valeur = self.element
        self.valeur = valeur
        self.valeur_critique = self.valeur
        self.cible = cible
        self.calcul = calcul
        self.cible_necessaire = self.cible in {TypeCible.UNE_CARTE,
                                               TypeCible.UNE_CARTE_ALLIEE,
                                               TypeCible.UNE_CARTE_ENNEMIE}
       
        self.p = 0.1
        self.duree = duree
        self.duree_critique = self.duree
        self.duree_infinie = False
        self.duree_tour = int(self.duree * 2)
        self.symbole = symbole
        self.nom = self.__class__.__name__
        self.choix = False
        self.choisi = False
        self.annuler = False

        if self.calcul != TypeCalcul.CLASSIQUE:
            self.nom += f"[{self.calcul.name}]"

        self.effet_defaut = copy.deepcopy(self)

    @abstractmethod
    def appliquer(self, 
                  carte_cible: Optional[Union["Attaque", "Carte", "Joueur"]], 
                  critique: int = 1) -> None:
        pass

    @abstractmethod
    def declencher(self, **donnees) -> None:
        pass

    def executer(self, *args, **kwargs) -> None:
        pass
    
    def mettre_a_jour_statut(self) -> None:
        pass

    def decrementer_duree(self) -> bool:
        self.duree_tour -= 1
        return self.duree_tour <= 0

    def calcul_bonus_element(self) -> int:

        if self.element is None:
            return 0
        
        if self.element == Element.ALEATOIRE:
            self.element_valeur = Element.aleatoire()
        elif self.element == Element.CARTE:
            self.element_valeur = self.attaque.carte.element

        self.attaque.element_precedent = self.element_valeur

        bonus = self.attaque.carte.joueur.elements.get(self.element_valeur, 0) if self.element_valeur else 0
        
        old_bonus = bonus
        carte = self.attaque.carte
        carte.multiplicateur = 1
        carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.CALCUL_BONUS, carte=carte)

        bonus *= carte.multiplicateur

        if carte.multiplicateur > 1:
            print(f"🔷 Le bonus élément {self.element_valeur.name} est multiplié par {carte.multiplicateur} ({old_bonus} -> {bonus})")

        terrain = self.attaque.carte.joueur.jeu.terrain
        if terrain:
            bonus += terrain[1] if terrain[0] == self.element_valeur else 0
        return bonus
    
    def calcul_valeur_element(self) -> int:
        bonus = self.calcul_bonus_element()
        valeur_element = int(self.calcul_valeur() * (1 + self.p * bonus))
        return valeur_element

    def calcul_valeur(self) -> Union[int, float]:
        if isinstance(self.valeur, list):
            if isinstance(self.valeur[0], int):
                return random.randint(min(self.valeur), max(self.valeur))
            elif isinstance(self.valeur[0], float):
                return random.uniform(min(self.valeur), max(self.valeur))
        else:
            return self.valeur

    def cartes_cibles(self, 
                      cible: TypeCible = TypeCible.SOI_MEME) -> List[Optional[Union["Attaque", "Carte", "Joueur"]]]:

        if cible == TypeCible.TOUS_LES_ENNEMIS:
            liste = self.attaque.carte.joueur.adversaire.liste_cartes_vivantes()
            random.shuffle(liste)
            return liste
        
        elif cible == TypeCible.TOUS_LES_ALLIES:
            liste = self.attaque.carte.joueur.liste_cartes_vivantes()
            random.shuffle(liste)
            return liste
        
        elif cible == TypeCible.ALEATOIRE_ENNEMI:
            ennemis = self.attaque.carte.joueur.adversaire.liste_cartes_vivantes()
            return [random.choice(ennemis)] if ennemis else []
        
        elif cible == TypeCible.ALEATOIRE_ALLIE:
            allies = self.attaque.carte.joueur.liste_cartes_vivantes()
            return [random.choice(allies)] if allies else []
        
        elif cible == TypeCible.ALEATOIRE_TOUTES_LES_CARTES:
            return [random.choice(self.attaque.carte.joueur.jeu.liste_cartes_vivantes())]
        
        elif cible == TypeCible.TOUTES_LES_CARTES:
            liste = self.attaque.carte.joueur.jeu.liste_cartes_vivantes()
            random.shuffle(liste)
            return liste
        
        elif cible == TypeCible.TOUTES_LES_CARTES_SAUF_SOI_MEME:
            liste = [carte for carte in self.attaque.carte.joueur.jeu.liste_cartes_vivantes() if carte != self.attaque.carte]
            random.shuffle(liste)
            return liste
        
        elif cible == TypeCible.SOI_MEME:
            return [self.attaque.carte]
        
        elif cible == TypeCible.JOUEUR:
            return [self.attaque.carte.joueur]
        
        elif cible == TypeCible.ADVERSAIRE:
            return [self.attaque.carte.joueur.adversaire]
        
        elif cible == TypeCible.TOUS_LES_JOUEURS:
            liste = self.attaque.carte.joueur.jeu.joueurs
            random.shuffle(liste)
            return liste
        
        elif cible == TypeCible.ATTAQUE:
            return [self.attaque]
        
        elif cible == TypeCible.AUCUNE:
            return [None]
        
        elif cible == TypeCible.UNE_CARTE or cible == TypeCible.UNE_CARTE_ALLIEE or cible == TypeCible.UNE_CARTE_ENNEMIE:
            print(f"❌ L'attaque {self.attaque.nom} nécesssite une cible")
            return None

    def test_cible(self, 
                   cible: Optional[Union["Attaque", "Carte", "Joueur"]], 
                   type_cible: TypeCible) -> bool:

        if isinstance(cible, Joueur):
            return type_cible in {TypeCible.ADVERSAIRE,
                                  TypeCible.JOUEUR,
                                  TypeCible.TOUS_LES_JOUEURS}
        
        elif isinstance(cible, Carte):
            return type_cible in {TypeCible.UNE_CARTE,
                                  TypeCible.UNE_CARTE_ALLIEE,
                                  TypeCible.UNE_CARTE_ENNEMIE,
                                  TypeCible.TOUS_LES_ENNEMIS,
                                  TypeCible.TOUS_LES_ALLIES,
                                  TypeCible.ALEATOIRE_ENNEMI,
                                  TypeCible.ALEATOIRE_ALLIE,
                                  TypeCible.ALEATOIRE_TOUTES_LES_CARTES,
                                  TypeCible.TOUTES_LES_CARTES,
                                  TypeCible.SOI_MEME}
        
        elif isinstance(cible, Attaque):
            return type_cible in {TypeCible.ATTAQUE}
        
        elif cible is None:
            pass

        return False

    def strategie_calcul(self, calcul: TypeCalcul = TypeCalcul.CLASSIQUE) -> int:

        if calcul == TypeCalcul.CLASSIQUE:
            return int(self.calcul_valeur_element())
        
        elif calcul == TypeCalcul.PV_MAX:
            carte = self.attaque.carte
            return int(self.calcul_valeur_element() + carte.pv_max / 10)
    
        elif calcul == TypeCalcul.PV_BAS:
            carte = self.attaque.carte
            return int(self.calcul_valeur_element() + (carte.pv_max - carte.pv) / 2)
        
        elif calcul == TypeCalcul.MULTIPLICATEUR_ELEMENT:
            return int(self.calcul_valeur() * self.calcul_bonus_element())

    def elements_bonus(self, joueur: "Joueur", element: Optional[Element] = None) -> List[Element]:

        if element is None:
            element = self.element

        if element == Element.MULTI:
            elements = Element.liste_elements()
        elif element == Element.ALEATOIRE:
            self.element_valeur = Element.aleatoire()
            elements = [self.element_valeur]
        elif element == Element.JOUEUR:
            elements = joueur.liste_elements_joueur()
        elif element == Element.CARTE:
            elements = [self.attaque.carte.element]
        elif element == Element.PRECEDENT:
            elements = [self.attaque.element_precedent]
        else:
            elements = [self.element]

        return elements

# --------------- COMPETENCES ------------------#

class DEGATS_ELEMENT(Effet):
    def __init__(self, 
                 valeur: Union[int, List[int]] = 0,
                 element: Optional[Element] = None, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE):
              
        super().__init__(valeur=valeur,
                         element=element,
                         cible=cible,
                         calcul=calcul)

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.strategie_calcul(self.calcul) * critique)
        self.executer(carte_cible, valeur_critique, self.element_valeur, self.attaque)

    def executer(self, carte: "Carte", valeur: int, element: Optional[Element] = None, attaque: Optional["Attaque"] = None, statut: bool = False) -> None:
        if attaque is None:
            attaque = self.attaque
        if carte.est_vivant():
            if valeur < 0:
                SOIN_ELEMENT().executer(carte, -valeur, element, attaque)
            elif valeur > 0:  
                old_pv = carte.pv
                carte.pv -= valeur
                carte.ajuster_pv()
                print(f"💥 {carte.nom} subit {valeur} dégâts {element.name + ' ' if element else ''}({old_pv} -> {carte.pv})")
                carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.APRES_DEGATS, carte=carte, attaque=attaque, valeur=valeur, statut=statut)
                if not carte.est_vivant():
                    carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.CARTE_MORTE, carte=carte, attaque=attaque)
            else:
                print(f"⭕ Aucun dégât subi par {carte.nom}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class SOIN_ELEMENT(Effet):
    def __init__(self, 
                 valeur: Union[int, List[int]] = 0,
                 element: Optional[Element] = None, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE):
              
        super().__init__(valeur=valeur, 
                         element=element,
                         cible=cible,
                         calcul=calcul)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.strategie_calcul(self.calcul) * critique)
        self.executer(carte_cible, valeur_critique, self.element_valeur, self.attaque)

    def executer(self, carte: "Carte", valeur: int, element: Optional[Element] = None, attaque: Optional["Attaque"] = None) -> None:
        if attaque is None:
            attaque = self.attaque
        if carte.est_vivant():
            if valeur < 0:
                DEGATS_ELEMENT().executer(carte, -valeur, element, attaque)
            elif valeur > 0:
                old_pv = carte.pv
                carte.pv += valeur
                carte.ajuster_pv()
                print(f"💚 {carte.nom} récupère {valeur} PV {element.name + ' ' if element else ''}({old_pv} -> {carte.pv})")
                carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.APRES_SOIN, carte=carte, attaque=attaque, valeur=valeur)
            else:
                print(f"⭕ Aucun soin appliqué à {carte.nom}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class BONUS_ELEMENT(Effet):
    def __init__(self, 
                 valeur: Union[int, List[int]] = 0,
                 element: Element = Element.ALEATOIRE, 
                 cible: TypeCible = TypeCible.JOUEUR):
              
        super().__init__(valeur=valeur, 
                         element=element, 
                         cible=cible,)

    def appliquer(self, 
                  joueur_cible: "Joueur", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)

        for element in self.elements_bonus(joueur_cible):
            self.executer(joueur_cible, valeur_critique, element, self.attaque)

    def executer(self, joueur: "Joueur", valeur: int, element: Element, attaque: Optional["Attaque"] = None) -> None:
        if attaque is None:
            attaque = self.attaque
        
        if element == Element.AUCUN or valeur == 0:
            print(f"⭕ Aucun bonus élémentaire obtenu par {joueur.nom}")     
        else:
            attaque.element_precedent = element
            old_element = joueur.elements[element]
            joueur.elements[element] = min(99, joueur.elements[element] + valeur)
            print(f"🔷 {joueur.nom} obtient {'+' if valeur >= 0 else ''}{valeur} en {element.name} ({old_element} -> {joueur.elements[element]})")
            joueur.jeu.gestion_evt.declencher(TypeEvenement.BONUS_ELEMENT, joueur=joueur, element=element, valeur=valeur, attaque=attaque)    

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class BONUS_RENIT(BONUS_ELEMENT):
    def __init__(self,
                 element: Element = Element.ALEATOIRE, 
                 cible: TypeCible = TypeCible.JOUEUR):
        super().__init__(element=element,
                         cible=cible)
        
    def appliquer(self, 
                  joueur_cible: "Joueur", 
                  critique: int = 1) -> None:

        for element in self.elements_bonus(joueur_cible):
            valeur_critique = -joueur_cible.elements[element]
            self.executer(joueur_cible, valeur_critique, element)  

class PROBA_PRECISION(Effet):
    def __init__(self, 
                 valeur: Union[float, List[float]] = 0.0, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 element_cond: Optional[Element] = None):
        
        super().__init__(cible=cible, 
                         valeur=valeur)
        self.element_cond = element_cond

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        valeur_critique = self.calcul_valeur() * critique

        if not self.element_cond or self.element_cond == self.attaque.element_precedent:
            self.executer(carte_cible, valeur_critique)
        else:
            print(f"❌ La condition de l'effet {self.nom} n'est pas remplie")
 

    def executer(self, carte: "Carte", valeur: float = 0.0) -> None:
        print(f"🎯 {carte.nom} voit sa précision modifiée de {'+' if valeur >= 0 else ''}{int(valeur*100)}%")
        for attaque in carte.attaques:
            old_precision = attaque.proba_precision
            attaque.proba_precision += valeur
            attaque.proba_precision = max(0.05, min(attaque.proba_precision, 1.0))
            print(f"\t- {attaque.nom} : {old_precision:.2f} -> {attaque.proba_precision:.2f}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class PROBA_CRITIQUE(Effet):
    def __init__(self, 
                 valeur: Union[float, List[float]] = 0.0, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 element_cond: Optional[Element] = None):
        
        super().__init__(valeur=valeur,
                         cible=cible)
        self.element_cond = element_cond

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        valeur_critique = self.calcul_valeur() * critique

        if not self.element_cond or self.element_cond == self.attaque.element_precedent:
            self.executer(carte_cible, valeur_critique)
        else:
            print(f"❌ La condition de l'effet {self.nom} n'est pas remplie")


    def executer(self, carte: "Carte", valeur: float = 0.0) -> None:
        print(f"⚡ {carte.nom} voit son taux de critique modifié de {'+' if valeur >= 0 else ''}{int(valeur*100)}%")
        for attaque in carte.attaques:
            old_critique = attaque.proba_critique
            attaque.proba_critique += valeur
            attaque.proba_critique = max(0.0, min(attaque.proba_critique, 1.0))
            print(f"\t- {attaque.nom} : {old_critique:.2f} -> {attaque.proba_critique:.2f}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class DEGATS_CRITIQUE(Effet):
    def __init__(self, 
                 valeur: Union[int, List[int]] = 1, 
                 cible: TypeCible = TypeCible.SOI_MEME):
        
        super().__init__(valeur=valeur,
                         cible=cible)

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)

        self.executer(carte_cible, valeur_critique)

    def executer(self, carte: "Carte", valeur: int = 0) -> None:
        print(f"💥 {carte.nom} voit sa valeur de critique modifiée")
        for attaque in carte.attaques:
            old_critique = attaque.critique
            attaque.critique += valeur
            attaque.critique = max(1, attaque.critique)
            print(f"\t- {attaque.nom} : x{old_critique} -> x{attaque.critique}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class VALEUR_DE_BASE(Effet):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         evenement=TypeEvenement.APRES_ATTAQUE)
        self.effets_autorises = ["DEGATS_ELEMENT", "SOIN_ELEMENT"]

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)
        
        print(f"🔥 {carte_cible.nom} voit la valeur de base de ses attaques modifée")
        for attaque in carte_cible.attaques:
            self.executer(attaque, valeur_critique)

    def executer(self, attaque: "Attaque", valeur: int = 0) -> None:
        affichage_attaque = False
        for effet in attaque.effets:
            if effet.nom in self.effets_autorises:

                if not affichage_attaque:
                    print(f"{'🔺' if valeur >= 0 else '🔻'} La valeur de base de {attaque.nom} est modifiée de {'+' if valeur >= 0 else ''}{valeur}")
                    affichage_attaque = True

                print(f"\t- {effet.nom} : ", end="")

                if isinstance(effet.valeur, list):
                    old_valeur = effet.valeur
                    effet.valeur = [val + valeur for val in effet.valeur]
                    print(f"{old_valeur} -> {effet.valeur}")
                else:
                    old_valeur = effet.valeur
                    effet.valeur += valeur
                    print(f"{old_valeur} -> {effet.valeur}")
        if not affichage_attaque:
            print(f"❌ La valeur de base de l'attaque {attaque.nom} ne peut pas être modifiée")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        attaque_rate = donnees.get("attaque_rate")

        if self.carte.est_vivant() and attaque.carte == self.carte and not any(attaque_rate):
            print(f"🔥 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.executer(attaque, self.calcul_valeur())

class DEGATS_POURCENTAGE(DEGATS_ELEMENT):
    def __init__(self, 
                 valeur: Union[float, List[float]] = 0.0, 
                 cible: TypeCible = TypeCible.SOI_MEME):
              
        super().__init__(valeur=valeur,
                         cible=cible)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        valeur_critique = int(self.calcul_valeur() * carte_cible.pv_max * critique)
        self.executer(carte_cible, valeur_critique, attaque=self.attaque)

class SOIN_POURCENTAGE(SOIN_ELEMENT):
    def __init__(self, 
                 valeur: Union[float, List[float]] = 0.0, 
                 cible: TypeCible = TypeCible.SOI_MEME):
              
        super().__init__(valeur=valeur,
                         cible=cible)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * carte_cible.pv_max * critique)
        self.executer(carte_cible, valeur_critique, attaque=self.attaque)

class VOL_ELEMENT(BONUS_ELEMENT):
    def __init__(self,
                 valeur: Union[int, List[int]] = 0,
                 element: Element = Element.ALEATOIRE,
                 cible: TypeCible = TypeCible.ADVERSAIRE):
        
        super().__init__(valeur=valeur,
                         element=element, 
                         cible=cible)

    def appliquer(self, 
                  joueur_cible: "Joueur", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)

        for element in self.elements_bonus(joueur_cible):
            self.executer(joueur_cible, -valeur_critique, element, self.attaque)
            self.executer(joueur_cible.adversaire, valeur_critique, element, self.attaque)

class RECHARGE_MAX(Effet):
    def __init__(self, 
                 cible: TypeCible = TypeCible.SOI_MEME):
              
        super().__init__(cible=cible)
         
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        self.executer(carte_cible)

    def executer(self, carte: "Carte") -> None:
        print(f"🧭 {carte.nom} voit ses temps de récharge augmentés au maximum")
        for attaque in carte.attaques:
            attaque.recharge_max()

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class RECHARGE_RENIT(Effet):
    def __init__(self, 
                 cible: TypeCible = TypeCible.SOI_MEME):
              
        super().__init__(cible=cible)
         
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        self.executer(carte_cible)

    def executer(self, carte: "Carte") -> None:
        print(f"⌛ {carte.nom} voit ses temps de récharge rénitialisés")
        for attaque in carte.attaques:
            attaque.recharge_renit()

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class PV_MAX(Effet):
    def __init__(self, 
                 valeur: Union[int, List[int]] = 0, 
                 cible: TypeCible = TypeCible.SOI_MEME,
                 element: Optional[Element] = None,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE):
              
        super().__init__(valeur=valeur,
                         cible=cible,
                         element=element,
                         calcul=calcul)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        valeur_critique = int(self.strategie_calcul(self.calcul) * critique)
        self.executer(carte_cible, valeur_critique, self.element_valeur, self.attaque)

    def executer(self, carte: "Carte", valeur: int = 0, element: Optional[Element] = None, attaque: Optional["Attaque"] = None) -> None:
        if attaque is None:
            attaque = self.attaque
        if carte.est_vivant():
            old_pv_max = carte.pv_max
            carte.pv_max = max(0, carte.pv_max + valeur)
            if valeur > 0:
                carte.pv += valeur
                carte.ajuster_pv()
                print(f"💖 {carte.nom} voit ses PV MAX augmentés de {valeur} {element.name + ' ' if element else ''}({old_pv_max} → {carte.pv_max})")
            elif valeur < 0:
                carte.ajuster_pv()
                print(f"💔 {carte.nom} voit ses PV MAX diminués de {-valeur} {element.name + ' ' if element else ''}({old_pv_max} → {carte.pv_max})")

                if not carte.est_vivant():
                    carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.CARTE_MORTE, carte=carte, attaque=attaque)
                
            else:
                print(f"⭕ {carte.nom} ne subit aucun changement de PV MAX")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class SACRIFICE(Effet):
    def __init__(self,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(cible=cible)

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        self.executer(carte_cible, self.attaque.carte, self.attaque)
    
    def executer(self, carte: "Carte", carte_joueur: "Carte", attaque: Optional["Attaque"] = None):
        print(f"💀 {carte.nom} est sacrifiée par {carte_joueur.nom}")
        valeur = carte.pv
        if attaque is None:
            attaque = self.attaque
        DEGATS_ELEMENT().executer(carte, valeur, attaque=attaque)
        PV_MAX().executer(carte_joueur, carte.pv_max, attaque=attaque)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class RESURRECTION(Effet):
    def __init__(self,
                 valeur: Union[float, List[float]] = 0.5,
                 cible: TypeCible = TypeCible.JOUEUR):
        
        super().__init__(valeur=valeur,
                         cible=cible)

    def appliquer(self, 
                  joueur_cible: "Joueur", 
                  critique: int = 1) -> None:

        valeur_critique = self.calcul_valeur() * critique
        self.executer(joueur_cible, valeur_critique)

    def executer(sef, joueur: "Joueur", valeur: float) -> None:
        if joueur.cartes_mortes:
            carte = joueur.cartes_mortes.pop(0)
            carte.pv += int(valeur * carte.pv_max)
            carte.ajuster_pv()
            print(f"🧬 {carte.nom} est ressuscitée avec {carte.pv}/{carte.pv_max} PV")
        else:
            print(f"❌ {joueur.nom} n'a pas de cartes mortes")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class RECHARGE_PROBA(Effet):
    def __init__(self,
                 valeur: Union[float, List[float]] = 0.5,
                 cible: TypeCible = TypeCible.SOI_MEME):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         evenement=TypeEvenement.APRES_ATTAQUE)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = self.calcul_valeur()
        for attaque in carte_cible.attaques:
            self.executer(attaque, valeur_critique)

    def executer(self, attaque: "Attaque", valeur: float) -> None:
        p_recharge = random.random()
        if p_recharge < valeur:
            print(f"⌛ L'attaque {attaque.nom} peut être réutilisée")
            attaque.recharge_actuelle = 0
            attaque.attaque_renit = True
        else:
            print(f"❌ L'effet {self.nom} rate")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        passif_attaque = donnees.get("passif_attaque")

        if passif_attaque and self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧭 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.executer(attaque, self.calcul_valeur())

class RECHARGE_MOD(Effet):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.SOI_MEME):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         evenement=TypeEvenement.APRES_ATTAQUE)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = self.calcul_valeur()
        for attaque in carte_cible.attaques:
            self.executer(attaque, valeur_critique)

    def executer(self, attaque: "Attaque", valeur: int) -> None:
        old_recharge = attaque.recharge
        attaque.recharge = max(0, attaque.recharge + valeur)
        print(f"⌛ L'attaque {attaque.nom} voit sa recharge modifiée : {old_recharge} -> {attaque.recharge}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        passif_attaque = donnees.get("passif_attaque")

        if passif_attaque and self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧭 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.executer(attaque, self.valeur)

class REPARTITION_PV(Effet):
    def __init__(self,
                 cible: TypeCible = TypeCible.JOUEUR):
        
        super().__init__(cible=cible)

    def appliquer(self,
                  joueur_cible: "Joueur",
                  critique: int = 1) -> None:
        
        self.executer(joueur_cible, self.attaque)

    def executer(self, joueur: "Joueur", attaque: Optional["Attaque"] = None):

        if attaque is None:
            attaque = self.attaque

        cartes = joueur.liste_cartes_vivantes()

        pv = np.mean([carte.pv for carte in cartes], dtype=int)
        pv_max = np.mean([carte.pv_max for carte in cartes], dtype=int)

        for carte in cartes:
            valeur_pv_max = pv_max - carte.pv_max
            PV_MAX().executer(carte, valeur_pv_max, attaque=attaque)
            valeur_pv = pv - carte.pv
            SOIN_ELEMENT().executer(carte, valeur_pv, attaque=attaque)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        print(f"❌ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} n'est pas implémenté")

class PV_POURCENTAGE(SOIN_ELEMENT):
    def __init__(self,
                 valeur: Union[float, List[float]] = 0.5,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(valeur=valeur,
                         cible=cible)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        pv = int(self.calcul_valeur() * carte_cible.pv_max)
        valeur_pv = pv - carte_cible.pv
        self.executer(carte_cible, valeur_pv, attaque=self.attaque)

class VOL_PV(DEGATS_ELEMENT):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.UNE_CARTE,
                 element: Optional[Element] = None,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         element=element,
                         calcul=calcul)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.strategie_calcul(self.calcul) * critique)
        self.executer(carte_cible, valeur_critique, self.element_valeur, self.attaque)
        self.executer(self.attaque.carte, -valeur_critique, self.element_valeur, self.attaque)

class VOL_PV_MAX(PV_MAX):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.UNE_CARTE,
                 element: Optional[Element] = None,
                 calcul: TypeCalcul = TypeCalcul.CLASSIQUE):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         element=element,
                         calcul=calcul)
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.strategie_calcul(self.calcul) * critique)
        self.executer(carte_cible, -valeur_critique, self.element_valeur, self.attaque)
        self.executer(self.attaque.carte, valeur_critique, self.element_valeur, self.attaque)


# ----------------------EFFETS---------------------- #

class CIMETIERE(Effet):
    def __init__(self,
                 valeur: int = 2):
        super().__init__(evenement=TypeEvenement.CARTE_MORTE,
                         valeur=valeur)
                         
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        if self.carte.est_vivant():
            print(f"⚰️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            joueur = self.carte.joueur
            for element in Element.liste_elements():
                BONUS_ELEMENT().executer(joueur, self.valeur, element, attaque=self) 

class CONTRECOUP(Effet):
    def __init__(self,
                 valeur: float = 0.5):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur)
        
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        valeur = donnees.get("valeur")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and attaque.carte == self.carte and attaque != self:
            print(f"💢 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            valeur_contre = int(valeur * self.valeur)
            DEGATS_ELEMENT().executer(self.carte, valeur_contre, attaque=self)

class FUMEE(Effet):
    def __init__(self):
        super().__init__(evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN, TypeEvenement.AVANT_ATTAQUE, TypeEvenement.AVANT_EFFET])
    
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        evenement = donnees.get("evenement")
        if evenement == TypeEvenement.AVANT_ATTAQUE:
            attaque.carte.fumee = False

        elif evenement == TypeEvenement.AVANT_EFFET:
            carte = donnees.get("carte")
            if hasattr(carte, "fumee"):
                carte.fumee = False
        else:
            if self.carte.est_vivant() and attaque.carte == self.carte and not self.carte.fumee:
                print(f"💨 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                random.shuffle(self.carte.joueur.cartes)
                for carte in self.carte.joueur.cartes:
                    carte.fumee = True
                print(f"❔ Les cartes de {self.carte.joueur.nom} sont désormais dissimulées")

class MIMETISME(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.BONUS_ELEMENT)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        joueur = donnees.get("joueur")
        valeur = donnees.get("valeur")
        element = donnees.get("element")
        attaque = donnees.get("attaque")

        if self.carte.est_vivant() and joueur != self.carte.joueur and attaque.__class__ != self.__class__:
            print(f"🔮 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            BONUS_ELEMENT().executer(self.carte.joueur, valeur, element, attaque=self)

class MULTIPLICATEUR(Effet):
    def __init__(self,
                 valeur: int = 2):
        super().__init__(evenement=TypeEvenement.CALCUL_BONUS,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and carte == self.carte:
            print(f"✖️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.carte.multiplicateur = self.valeur

class POISON(Effet):
    def __init__(self,
                 valeur: float = 0.03,
                 duree: int = 3):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur,
                         duree=duree,
                         symbole="🧪")
        
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        statut = donnees.get("statut")
        if carte.est_vivant() and self.carte.est_vivant() and attaque.carte == self.carte and attaque.__class__ != self.__class__ and not statut:
            print(f"☠️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.attaque = attaque
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                carte.ajout_statut(self)

    def mettre_a_jour_statut(self, carte: "Carte") -> None:
        if self.duree_tour % 2 == 0:
            valeur = int(self.valeur * carte.pv_max)
            DEGATS_ELEMENT().executer(carte, valeur, attaque=self.attaque, statut=True)
        if self.decrementer_duree():
            carte.retirer_statut(self)

class POISON_EX(POISON):
    def __init__(self,
                 valeur: float = 0.03,
                 duree: int = 999999):
        super().__init__(valeur=valeur,
                         duree=duree)
        self.duree_infinie = True

class RENVOI(Effet):
    def __init__(self,
                 valeur: float = 0.1):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        carte = donnees.get("carte")
        valeur = donnees.get("valeur")
        attaque = donnees.get("attaque")
        if carte == self.carte and attaque.carte != self.carte:
            print(f"🪞  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            valeur_renvoi = int(valeur * self.valeur)
            DEGATS_ELEMENT().executer(attaque.carte, valeur_renvoi, attaque=self)

class RENVOI_EX(RENVOI):
    def __init__(self,
                 valeur: float = 0.5):
        super().__init__(valeur=valeur)

class RESET(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.CARTE_MORTE)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte and carte.joueur != self.carte.joueur:
            print(f"♻️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            RECHARGE_PROBA().executer(attaque, valeur=1.0)

class RESET_EX(RESET):
    def __init__(self):
        super().__init__()

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte and carte.joueur != self.carte.joueur:
            print(f"♻️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            RECHARGE_RENIT().executer(self.carte)
            attaque.attaque_renit = True

class REVANCHE(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.CARTE_MORTE)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        if not self.carte.est_vivant() and carte == self.carte:
            print(f"👊 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            RECHARGE_RENIT().executer(self.carte)
            for atq in self.carte.attaques:
                if not atq.cible_necessaire:
                    atq.attaquer()
                else:
                    atq.attaquer(attaque.carte)

class SAC_DE_FRAPPE(Effet):
    def __init__(self,
                 valeur: int = 1):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        if carte == self.carte and attaque.carte != self.carte:
            print(f"🥊 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            BONUS_ELEMENT().executer(self.carte.joueur, self.valeur, self.carte.element, attaque=self)

class SOIN_PRIMITIF(Effet):
    def __init__(self,
                 valeur: float = 0.03):
        super().__init__(evenement=TypeEvenement.DEBUT_TOUR,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        joueur = donnees.get("joueur")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and self.carte.joueur == joueur and not self.carte.vie_entiere():
            print(f"🌱 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            valeur_soin = int(self.valeur * self.carte.pv_max)
            SOIN_ELEMENT().executer(self.carte, valeur_soin, attaque=self)

class TERRAIN(Effet):
    def __init__(self,
                 valeur: int = 5):
        super().__init__(evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN],
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        jeu = self.carte.joueur.jeu
        if self.carte.est_vivant() and attaque.carte == self.carte:
            terrain_element = jeu.terrain[0] if jeu.terrain else None
            if terrain_element != self.carte.element:
                print(f"🌍 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                jeu.appliquer_terrain(self.valeur, self.carte.element)

class TENACITE(Effet):
    def __init__(self):
        super().__init__(evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])
        self.utilise = False

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        evenement = donnees.get("evenement")
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")

        if carte == self.carte:

            if evenement == TypeEvenement.APRES_DEGATS:
                if not self.carte.est_vivant() and not self.utilise:
                    print(f"💪 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                    print(f"💚 {carte.nom} survit à 1 PV")
                    self.carte.pv = 1
                    self.utilise = True

            elif evenement == TypeEvenement.APRES_SOIN:
                if self.carte.est_vivant() and self.carte.vie_entiere():
                    print(f"💪 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                    self.utilise = False

class VAMPIRISME(Effet):
    def __init__(self,
                 valeur: float = 0.5):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        valeur = donnees.get("valeur")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🩸 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            valeur_vampirisme = int(valeur * self.valeur)
            SOIN_ELEMENT().executer(self.carte, valeur_vampirisme, attaque=self)

class VENGEUR(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.CARTE_MORTE)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and attaque.carte != self.carte:
            print(f"⚔️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            RECHARGE_RENIT().executer(self.carte)

class EROSION(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        valeur = donnees.get("valeur")
        if self.carte.est_vivant() and attaque.carte == self.carte and carte.est_vivant():
            print(f"🪓 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            PV_MAX().executer(carte, -valeur, attaque=self)

class ZONE(Effet):
    def __init__(self,
                 valeur: float = 0.5):
        super().__init__(evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN],
                         valeur=valeur)
        
    def cartes_voisines(self, carte: "Carte", rayon: int = 1) -> List["Carte"]:
        voisines = []
        cartes = carte.joueur.cartes
        place = cartes.index(carte)

        for index in range(-rayon, rayon + 1):
            if index == 0:
                continue
            index_voisin = place + index

            if 0 <= index_voisin < len(cartes):
                carte_voisine = cartes[index_voisin]

                if carte_voisine.est_vivant():
                    voisines.append(carte_voisine)

        return voisines
        
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        valeur = donnees.get("valeur")
        evenement = donnees.get("evenement")
        if self.carte.est_vivant() and attaque.carte == self.carte and attaque != self:
            print(f"🌊 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            cartes_voisines = self.cartes_voisines(carte)
            valeur_zone = int(valeur * self.valeur)
            for carte in cartes_voisines:
                if evenement == TypeEvenement.APRES_DEGATS:
                    effet = DEGATS_ELEMENT()
                elif evenement == TypeEvenement.APRES_SOIN:
                    effet = SOIN_ELEMENT()
                effet.executer(carte, valeur_zone, attaque=self)

class CROISSANCE(Effet):
    def __init__(self,
                 valeur: float = 1.0):
        super().__init__(evenement=TypeEvenement.APRES_DEGATS,
                         valeur=valeur)

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        valeur = donnees.get("valeur")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🌟 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            valeur_croissance = int(valeur * self.valeur)
            PV_MAX().executer(self.carte, valeur_croissance, attaque=self)

class MYSTERE(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.DEBUT_JEU)

        self.passifs = {
            CIMETIERE,
            CONTRECOUP,
            DISPARITION,
            FUMEE,
            IMMUNITE,
            IMMUNITE_EX,
            MIMETISME,
            MULTIPLICATEUR,
            POISON,
            POISON_EX,
            PURGE,
            RENVOI,
            RENVOI_EX,
            RESET,
            RESET_EX,
            REVANCHE,
            SAC_DE_FRAPPE,
            SOIN_PRIMITIF,
            TEMPORALITE,
            TERRAIN,
            TENACITE,
            VAMPIRISME,
            VENGEUR,
            EROSION,
            ETERNITE,
            ETOURDISSEMENT
        }
                        
    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        if self.carte.est_vivant():
            print(f"❓ Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")

            passif_mystere = random.choice(list(self.passifs))()
            passif_mystere.carte = self.carte

            index = self.carte.passifs.index(self)
            self.carte.passifs[index] = passif_mystere

            self.carte.joueur.jeu.initialisation_passifs()

            print(f"🍀 {self.carte.nom} obtient le passif {passif_mystere.nom}")

class IMMUNITE(Effet):
    def __init__(self):
        super().__init__(evenement=TypeEvenement.AVANT_EFFET)

        self.effets_immunises = {DISPARITION,
                                PROBA_PRECISION,
                                PROBA_CRITIQUE,
                                DEGATS_CRITIQUE,
                                TEMPORALITE,
                                ETERNITE,
                                RECHARGE_MAX,
                                RECHARGE_RENIT,
                                PROVOCATION,
                                ETOURDISSEMENT,
                                VALEUR_DE_BASE,
                                PURGE}

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        effet = donnees.get("effet")
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and carte == self.carte and effet.attaque.carte.joueur != self.carte.joueur:

            if effet.__class__ in self.effets_immunises:
                
                print(f"🔒 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                effet.annuler = True

class IMMUNITE_EX(IMMUNITE):
    def __init__(self):
        super().__init__()

    def declencher(self, **donnees) -> None:
        effet = donnees.get("effet")
        carte = donnees.get("carte")
        attaque = donnees.get("attaque")
        if self.carte.est_vivant() and carte in self.carte.joueur.liste_cartes_vivantes() and effet.attaque.carte.joueur != self.carte.joueur:

            if effet.__class__ in self.effets_immunises:
                
                print(f"🔒 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                effet.annuler = True

class DISPARITION(Effet):
    def __init__(self,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(cible=cible,
                         evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        self.executer(carte_cible)

    def executer(self, carte: "Carte") -> None:
        if carte.passifs:
            passif_supprime = carte.passifs.pop()
            carte.passifs_suppr.append(passif_supprime)
            print(f"👻 {carte.nom} perd le passif {passif_supprime.nom}")
            carte.joueur.jeu.initialisation_passifs()
        elif carte.attaques:
            attaque_supprimee = carte.attaques.pop()
            carte.attaques_suppr.append(attaque_supprimee)
            print(f"👻 {carte.nom} perd l'attaque {attaque_supprimee.nom}")
        else:
            print(f"❌ {carte.nom} n'a plus de compétences à supprimer")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if attaque.carte == self.carte:
            print(f"🗑️  Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                self.executer(carte)  

class PROVOCATION(Effet):
    def __init__(self,
                 duree: int = 1,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(duree=duree, 
                         cible=cible,
                         symbole = "🛡️ ",
                         evenement=TypeEvenement.APRES_SOIN)

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        self.duree_critique = int(self.duree * critique)
        carte_cible.ajout_statut(self)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        attaque_rate = donnees.get("attaque_rate")

        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧲 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:    
                carte.ajout_statut(self)
 
    def mettre_a_jour_statut(self, carte: "Carte") -> None:
        if self.decrementer_duree():
            carte.retirer_statut(self) 

class PURGE(Effet):
    def __init__(self,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(cible=cible,
                         evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])

    def appliquer(self, 
                  carte_cible: "Carte" = None, 
                  critique: int = 1) -> None:
        
        self.executer(carte_cible)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧽 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                self.executer(carte)

    def executer(self, carte: "Carte") -> None:

        print(f"🧼 {carte.nom} est purgée de tous les effets")

        attributs_carte = ["pv_max", "statut", "attaques_suppr", "passifs_suppr", "fumee"]
        attributs_attaque = ["proba_precision", "proba_critique", "critique", "recharge"]
        attributs_effet = ["valeur"]

        for attaque_suppr in carte.attaques_suppr:
            carte.attaques.append(attaque_suppr)

        for passif_suppr in carte.passifs_suppr:
            carte.passifs.append(passif_suppr)

        carte.joueur.jeu.initialisation_passifs()

        for attribut in attributs_carte:
            setattr(carte, attribut, getattr(carte.carte_defaut, attribut))
        carte.ajuster_pv()

        for attaque in carte.attaques:
            for attribut in attributs_attaque:
                setattr(attaque, attribut, getattr(attaque.attaque_defaut, attribut))
            attaque.ajuster_recharge()

            for effet in attaque.effets:
                for attribut in attributs_effet:
                    setattr(effet, attribut, getattr(effet.effet_defaut, attribut))

class TEMPORALITE(Effet):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.SOI_MEME):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)
        self.executer(carte_cible, valeur_critique)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧭 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                self.executer(carte, self.valeur)

    def executer(self, carte: "Carte", n: int = 1) -> None:
        affichage = False 
        for attaque in carte.attaques:
            for _ in range(n):
                if attaque.recharge_actuelle > 0:
                    if not affichage:
                        print(f"⌛ {carte.nom} voit ses temps de récharge diminués")
                        affichage = True
                    old_recharge = attaque.recharge_actuelle
                    attaque.recharge_actuelle -= 1
                    attaque.ajuster_recharge()
                    print(f"\t- {attaque.nom} : {old_recharge} -> {attaque.recharge_actuelle}")

class ETERNITE(Effet):
    def __init__(self,
                 valeur: Union[int, List[int]] = 1,
                 cible: TypeCible = TypeCible.SOI_MEME):
        
        super().__init__(valeur=valeur,
                         cible=cible,
                         evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])

    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:
        
        valeur_critique = int(self.calcul_valeur() * critique)
        self.executer(carte_cible, valeur_critique)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧭 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                self.executer(carte, self.valeur)

    def executer(self, carte: "Carte", n: int = 1) -> None:
        print(f"⌛ {carte.nom} voit ses temps de récharge augmentés")
        for attaque in carte.attaques:
            for _ in range(n):
                old_recharge = attaque.recharge_actuelle
                attaque.recharge_actuelle += 1
                print(f"\t- {attaque.nom} : {old_recharge} -> {attaque.recharge_actuelle}")

class ETOURDISSEMENT(Effet):
    def __init__(self,
                 duree: int = 1,
                 cible: TypeCible = TypeCible.UNE_CARTE):
        
        super().__init__(duree=duree, 
                         cible=cible,
                         symbole="💫",
                         evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])
        
    def appliquer(self, 
                  carte_cible: "Carte", 
                  critique: int = 1) -> None:

        self.duree_critique = int(self.duree * critique)
        carte_cible.ajout_statut(self)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        carte = donnees.get("carte")
        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧊 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            
            if any(passif.__class__ == IMMUNITE for passif in carte.passifs):
                print(f"🔒 Le passif IMMUNITE de {carte.nom} se déclenche")
                print(f"❌ {carte.nom} est immunisée contre l'effet {self.nom}")
            else:
                carte.ajout_statut(self)

    def mettre_a_jour_statut(self, carte: "Carte") -> None:
        if self.decrementer_duree():
            carte.retirer_statut(self)

class COUT(Effet):
    def __init__(self,
                 cout: Dict = {}):
        super().__init__(evenement=[TypeEvenement.DEBUT_JEU, TypeEvenement.CHOIX_ATTAQUE, TypeEvenement.APRES_ATTAQUE])
        self.cout = cout

    def affichage_cout(self, attaque: "Attaque") -> None:
        for i, (element, valeur) in enumerate(attaque.cout.items()):
            end = " | "
            if i == len(attaque.cout) - 1:
                end = ""
            if element == "PV":
                element = element
            else:
                element = element.name
            print(valeur, element, end=end)

    def test_cout(self, attaque: "Attaque") -> bool:
        for element, valeur in attaque.cout.items():
            if element == "PV":
                if valeur != "TOUS" and attaque.carte.pv < valeur:
                    print("❌ Cette attaque nécessite un coût : ", end="")
                    self.affichage_cout(attaque)
                    return False
            else:
                bonus = attaque.carte.joueur.elements.get(element, 0)
                if (valeur == "TOUS" and bonus <= 0) or (valeur != "TOUS" and bonus < valeur):
                    print("❌ Cette attaque nécessite un coût : ", end="")
                    self.affichage_cout(attaque)
                    return False
        return True

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def executer(self, attaque: "Attaque") -> None:
        for element, valeur in attaque.cout.items():
            if element == "PV":
                if valeur == "TOUS":
                    montant = attaque.carte.pv
                else:
                    montant = valeur
                DEGATS_ELEMENT().executer(attaque.carte, montant, attaque=attaque)

            else:
                if valeur == "TOUS":
                    montant = attaque.carte.joueur.elements.get(element, 0)
                else:
                    montant = valeur
                BONUS_ELEMENT().executer(attaque.carte.joueur, -montant, element, attaque=attaque)

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        evenement = donnees.get("evenement")
        passif_attaque = donnees.get('passif_attaque')

        if passif_attaque and self.carte.est_vivant() and attaque.carte == self.carte and self.cout:
            
            if evenement == TypeEvenement.DEBUT_JEU:
                attaque.cout = self.cout

            elif evenement == TypeEvenement.CHOIX_ATTAQUE:
                attaque.valide &= self.test_cout(attaque)

            elif evenement == TypeEvenement.APRES_ATTAQUE and attaque.cout:
                print(f"💎 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                self.executer(attaque)

class USAGE_LIMITE(Effet):
    def __init__(self,
                 usage_limite: int = 0):
        super().__init__(evenement=[TypeEvenement.DEBUT_JEU, TypeEvenement.CHOIX_ATTAQUE, TypeEvenement.APRES_ATTAQUE])
        self.usage_limite = usage_limite
        self.usage = self.usage_limite

    def test_usage_limite(self, attaque: "Attaque") -> bool:
        if attaque.usage_limite:
            if attaque.usage > 0:
                return True
            else:
                print(f"❌ Cette attaque est à usage limité : {attaque.usage}/{attaque.usage_limite}")
                return False
        else:
            return True
        
    def executer(self, attaque: "Attaque", n: int = 1) -> None:
        if attaque.usage_limite:
            old_usage = attaque.usage
            attaque.usage -= n
            print(f"🪫  L'attaque {attaque.nom} perd {n} utilisation{'s' if n > 1 else ''} ({old_usage} -> {attaque.usage})")

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        evenement = donnees.get("evenement")
        passif_attaque = donnees.get('passif_attaque')

        if passif_attaque and self.carte.est_vivant() and attaque.carte == self.carte and self.usage_limite:
            
            if evenement == TypeEvenement.DEBUT_JEU:
                attaque.usage_limite = self.usage_limite
                attaque.usage = self.usage

            elif evenement == TypeEvenement.CHOIX_ATTAQUE:
                attaque.valide &= self.test_usage_limite(attaque)

            elif evenement == TypeEvenement.APRES_ATTAQUE and attaque.usage_limite:
                print(f"🧨 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                self.executer(attaque)

class ALEATOIRE(Effet):
    def __init__(self):
        super().__init__(evenement=[TypeEvenement.DEBUT_JEU, TypeEvenement.AVANT_ATTAQUE])

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def cible_aleatoire(self, cible: TypeCible) -> TypeCible:
        if cible == TypeCible.UNE_CARTE:
            return TypeCible.ALEATOIRE_TOUTES_LES_CARTES
        elif cible == TypeCible.UNE_CARTE_ALLIEE:
            return TypeCible.ALEATOIRE_ALLIE
        elif cible == TypeCible.UNE_CARTE_ENNEMIE:
            return TypeCible.ALEATOIRE_ENNEMI
        else:
            return cible
        
    def executer(self, attaque: "Attaque") -> None:
        pass            

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")
        passif_attaque = donnees.get('passif_attaque')
        evenement = donnees.get('evenement')

        if passif_attaque and attaque.carte == self.carte:

            if evenement == TypeEvenement.DEBUT_JEU:
                attaque.cible_necessaire = False
                for effet in attaque.effets + attaque.effets_critiques + attaque.effets_passifs:
                    effet.cible = self.cible_aleatoire(effet.cible)
                    effet.cible_necessaire = False

            elif evenement == TypeEvenement.AVANT_ATTAQUE:
                print(f"🎲 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
                self.executer(attaque)

class MYTHIQUE(Effet):
    def __init__(self):
        super().__init__(evenement=[TypeEvenement.APRES_DEGATS, TypeEvenement.APRES_SOIN])

    def appliquer(self, carte_cible: "Carte", critique: int = 1) -> None:
        print(f"❌ L'effet {self.nom} de {self.attaque.nom} n'est pas implémenté")

    def executer(self, carte: "Carte"):
        old_element = carte.element
        carte.element = Element.aleatoire()
        print(f"✨ La carte {carte.nom} passe de l'élément {old_element.name} à l'élément {carte.element.name}")

    def declencher(self, **donnees) -> None:
        attaque = donnees.get("attaque")

        if self.carte.est_vivant() and attaque.carte == self.carte:
            print(f"🧬 Le passif {self.nom} de {attaque.nom if donnees.get('passif_attaque') else self.carte.nom} se déclenche")
            self.executer(self.carte)


































