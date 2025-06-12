from utils import *

if TYPE_CHECKING:
    from carte import Carte

class Joueur:
    def __init__(self,
                 nom: str = "Joueur",
                 cartes: Optional[List["Carte"]] = None):

        self.nom = nom
        self.cartes = cartes if cartes is not None else []
        self.elements = {element: 0 for element in Element.liste_elements()}
        self.adversaire = None
        for carte in self.cartes:
            carte.joueur = self
        self.jeu = None
        self.cartes_mortes = []

        # print(f"Joueur créé : {self.nom} avec {len(self.cartes)} carte(s)")

    def ajouter_carte_morte(self, carte: "Carte") -> None:
        self.cartes_mortes.append(carte)

    def liste_elements_joueur(self) -> List[Element]:
        elements = list({carte.element for carte in self.cartes})
        return elements

    def affichage_elements(self) -> None:
        print(self.nom, end=" | ")
        for key, value in self.elements.items():
            print(f"{key.name}: {value}", end="  ")

    def affichage_cartes(self, joueur: "Joueur") -> None:

        for carte in self.liste_cartes_vivantes():
            if joueur != self and carte.fumee:
                print(carte_fumee, end="\n\n")
            else:
                print(f"{carte.numero} - {carte.nom} : {carte.pv}/{carte.pv_max} ({int(round(carte.pv / carte.pv_max * 100))}%)", end=" ")
                carte.affichage_statut()
                print("")
                for attaque in carte.attaques:
                    print(f"\t {attaque.nom}", end=" ")

                    if attaque.usage_limite:
                        print(f"{'[' + str(attaque.usage) + '/' + str(attaque.usage_limite) + ']'}", end=" ")

                    if attaque.cout:
                        from src.effet import COUT
                        print("[", end="") 
                        COUT().affichage_cout(attaque)
                        print("]", end=" ")

                    print(f": {attaque.recharge_actuelle}/{attaque.recharge}")
                for passif in carte.passifs:
                    print(f"\t \x1B[3m{passif.nom}\x1B[0m")

    def est_vivant(self) -> bool:
        vivant = any(carte.est_vivant() for carte in self.cartes)
        # print(f"{self.nom} est {'vivant' if vivant else 'KO'}")
        return vivant
    
    def liste_cartes_mortes(self) -> List["Carte"]:
        return [c for c in self.cartes if not c.est_vivant()]

    def liste_cartes_mortes_string(self) -> List[str]:
        return [f"{c.nom} | {c.pv}/{c.pv_max} | ({self.nom})"  for c in self.cartes if not c.est_vivant()]

    def liste_cartes_vivantes(self) -> List["Carte"]:
        return [c for c in self.cartes if c.est_vivant()]

    def liste_cartes_vivantes_string(self) -> List[str]:
        return [f"{c.nom} | {c.pv}/{c.pv_max} | ({self.nom})"  for c in self.cartes if c.est_vivant()]
    
    def decrementer_recharge(self, n: int = 1) -> None:
        from src.effet import TEMPORALITE
        for carte in self.cartes:
            TEMPORALITE().executer(carte, n)