from utils import *

if TYPE_CHECKING:
    from attaque import Attaque
    from effet import Effet

class Carte:
    def __init__(self,
                 nom: str = "",
                 numero: int = 1,
                 rarete: TypeRarete = TypeRarete.COMMUNE,
                 pv: int = 100,
                 element: Element = Element.EAU,
                 attaques: Optional[List["Attaque"]] = None,
                 passifs: Optional[List["Effet"]] = None):

        self.nom = nom
        self.numero = numero
        self.rarte = rarete
        self.pv = pv
        self.pv_max = pv
        self.element = element
        self.attaques = attaques if attaques is not None else []
        self.passifs = passifs if passifs is not None else []
        self.attaques_suppr = []
        self.passifs_suppr = []
        self.joueur = None
        self.fumee = False
        self.multiplicateur = 1
        for attaque in self.attaques:
            attaque.carte = self
            for effet_passif in attaque.effets_passifs:
                effet_passif.carte = self
        for passif in self.passifs:
            passif.carte = self
        if not self.nom:
            self.nom = f"Carte {self.numero}"

        self.statut: List["Effet"] = []

        self.carte_defaut = copy.deepcopy(self)

        # print(f"Carte créée : {self.nom} (PV: {self.pv})")

    def mise_a_jour_statut(self) -> None:
        for effet in self.statut:
            effet.mettre_a_jour_statut(self)

    def retirer_statut(self, effet: "Effet") -> None:
        if effet in self.statut:
            self.statut.remove(effet)
            print(f"{effet.symbole} {self.nom} n'a plus le statut {effet.nom}")

    def test_statut(self, effet: "Effet") -> bool:
        liste = [statut.__class__ for statut in self.statut if statut.duree_tour >= effet.duree_tour]
        test = effet.__class__ in liste
        return test
    
    def ajout_statut(self, effet: "Effet") ->None:

        if self.test_statut(effet):
            print(f"❌ {self.nom} a déjà le statut {effet.nom} ce tour")
        
        else:
            effet.duree_tour = int(effet.duree_critique * 2)
            self.statut = [s for s in self.statut if not isinstance(s, type(effet))]

            effet_copie = copy.deepcopy(effet)
            effet_copie.attaque = effet.attaque
            self.statut.append(effet_copie)
            print(f"{effet.symbole} {self.nom} obtient le statut {effet.nom} " + ("de façon permanente" if effet.duree_infinie else f"pendant {effet.duree_critique} tour{'s' if effet.duree_critique > 1 else ''}"))

   
    def affichage_statut(self) -> None:
        for effet in self.statut:
            print(effet.symbole, end=" ")

    def ajuster_pv(self) -> None:
        self.pv = max(0, min(self.pv, self.pv_max))

    def vie_entiere(self) -> bool:
        return self.pv == self.pv_max
    
    def est_vivant(self) -> bool:
        return self.pv > 0

    def liste_attaques_string(self) -> List[str]:
        return [f"{a.nom} | {a.recharge_actuelle}/{a.recharge}" for a in self.attaques]

    def liste_attaques_dispo(self) -> List["Attaque"]:
        return [a for a in self.attaques if a.test_recharge()]

    def liste_attaques_dispo_string(self) -> List[str]:
        return [f"{a.nom} | {a.recharge_actuelle}/{a.recharge}" for a in self.attaques if a.test_recharge()]