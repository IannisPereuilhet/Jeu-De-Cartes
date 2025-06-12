from utils import *

if TYPE_CHECKING:
    from effet import Effet
    from carte import Carte
    from joueur import Joueur


class Attaque:
    def __init__(self,
                 nom: str = "",
                 effets: Optional[List["Effet"]] = None,
                 effets_critiques : Optional[List["Effet"]] = None,
                 effets_passifs : Optional[List["Effet"]] = None,
                 proba_precision: float = 1.0,
                 proba_critique: float = 0.01,
                 critique: int = 1,
                 recharge: int = 1,
                 element: Element = Element.EAU,
                 info: str = ""):

        self.nom = nom
        self.proba_precision = proba_precision
        self.proba_critique = proba_critique
        self.critique = critique
        self.element = element
        self.element_precedent = element
        self.cout = {}
        self.valide = True
        self.effets_avec_choix = effets
        self.effets = self.effets_choix(effets)
        self.effets_critiques = effets_critiques if effets_critiques is not None else []
        self.effets_passifs = effets_passifs if effets_passifs is not None else []
        self.recharge = recharge
        self.recharge_actuelle = recharge
        self.usage_limite = 0
        self.usage = self.usage_limite
        self.info = info
        self.carte = None
        self.liste_elements = list({effet.element for effet in self.effets if effet.element})
        self.attaque_renit = False

        self.effets_noms = []
        for effet in self.effets:
            effet.attaque = self
            self.effets_noms.append(effet.nom)
        
        self.effets_critiques_noms = []
        for effet_critique in self.effets_critiques:
            effet_critique.attaque = self
            self.effets_critiques_noms.append(effet_critique.nom)

        self.effets_passifs_noms = []
        for effet_passif in self.effets_passifs:
            effet_passif.carte = None
            effet_passif.attaque = self
            self.effets_passifs_noms.append(effet_passif.nom)

        self.cible_necessaire = self.test_cible_necessaire()
        self.attaque_a_choix = self.test_attaque_a_choix()
        self.effets_passifs_evt = {e: [] for e in TypeEvenement}

        self.initialisation_passifs()

        if not self.nom:    
            self.nom = self.nom_attaque()

        self.attaque_defaut = copy.deepcopy(self)   

    def initialisation_passifs(self) -> None:
        for passif in self.effets_passifs:
            evenements = passif.evenement if isinstance(passif.evenement, list) else [passif.evenement]
            for evenement in evenements:
                if evenement:
                    self.effets_passifs_evt[evenement].append(passif)

    def recharge_attaque(self) -> None:
        if self.attaque_renit:
            self.attaque_renit = False
        else:
            self.recharge_max()

    def nom_attaque(self) -> str:
        morceaux = []
        for effet in self.effets_avec_choix:
            if isinstance(effet, list):
                morceau = "/".join(e.nom for e in effet)
            else:
                morceau = effet.nom
            morceaux.append(morceau)
        nom = "+".join(morceaux)

        for passif in reversed(self.effets_passifs):
            nom = f"{passif.nom}({nom})"
        return nom

    def reinitialiser_choix(self) -> None:
        for effet in self.effets:
            if effet.choisi:
                effet.choisi = False
                effet.choix = True

    def effets_choix(self, effets: Optional[List["Effet"]]) -> List["Effet"]:

        liste_effets = []
        compteur = 0

        if effets is not None:
            for effet in effets:
                if isinstance(effet, list):
                    compteur += 1
                    for e in effet:
                        e.choix = True
                        liste_effets.append(e)
                else:
                    effet.choix = False
                    liste_effets.append(effet)

        if not compteur:
            # print(f"Ce n'est pas une attaque à choix")
            pass
        elif compteur == 1:
            print(f"⚠️  {self.nom}({self.element.name}) est mal définie")
        else:
            # print(f"{self.nom}({self.element.name}) est une attaque à choix")
            pass
        
        return liste_effets
    
    def ajuster_recharge(self) -> None:
        self.recharge_actuelle = max(0, min(self.recharge_actuelle, self.recharge))

    def recharge_max(self) -> None:
        print(f"⌛ L'attaque {self.nom} se recharge")
        self.recharge_actuelle = self.recharge

    def recharge_renit(self) -> None:
        print(f"\t- L'attaque {self.nom} se rénitialise")
        self.recharge_actuelle = 0

    def test_attaque_a_choix(self) -> bool:
        return any(effet.choix for effet in self.effets)
    
    def test_cible_necessaire(self) -> bool:
        return any(effet.cible_necessaire for effet in self.effets)

    def test_recharge(self) -> bool:
        return self.recharge_actuelle == 0

    def fin_attaque(self) -> None:
        
        self.reinitialiser_choix()

        self.recharge_attaque()

    def declencher_evt_cible(self, cible: Union["Carte", "Joueur"], evenement: TypeEvenement, **donnees):
        if hasattr(cible, "joueur"):
            cible.joueur.jeu.gestion_evt.declencher(evenement, **donnees)
        elif hasattr(cible, "jeu"):
            cible.jeu.gestion_evt.declencher(evenement, **donnees)

    def appliquer_effets(self, carte_cible: Optional["Carte"] = None) -> None:

        self.carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.AVANT_ATTAQUE, attaque=self)
        effet_applique_sur = set()
        attaque_rate = []
        for effet in [e for e in self.effets if not e.choix]:

            cartes_cible = [carte_cible] if effet.cible_necessaire else effet.cartes_cibles(effet.cible)
            effet_copie = effet

            for cible in [c for c in cartes_cible if c.est_vivant()]:

                p_precision = random.random()
                p_critique = random.random()

                test_precision = p_precision > self.proba_precision
                attaque_rate.append(test_precision)

                if test_precision:
                    print(f"❌ L'effet {effet_copie.nom} {'sur ' + cible.nom + ' ' if cible else ''}rate")
                    continue
                
                print(f"✨ Effet appliqué {'sur ' + cible.nom + ' ' if cible else ''}: {effet_copie.nom}")

                self.declencher_evt_cible(cible, TypeEvenement.AVANT_EFFET, attaque=self, carte=cible, effet=effet)

                if effet.annuler:
                    effet.annuler = False
                    print(f"❌ {cible.nom} est immunisée contre l'effet {effet_copie.nom}")
                    continue

                test_crit = p_critique < self.proba_critique
                degats_critique = self.critique if test_crit else 1

                if test_crit:
                    print(f"⚡ Coup critique sur l'effet {effet_copie.nom} (x{degats_critique})")
                    
                effet_copie.appliquer(cible, degats_critique)
                effet_copie = copy.deepcopy(effet)
                effet_copie.attaque = self

                self.declencher_evt_cible(cible, TypeEvenement.APRES_EFFET, attaque=self, carte=cible, effet=effet)

                if cible not in effet_applique_sur:
                    self.declencher_evt_cible(cible, TypeEvenement.APRES_UN_EFFET, attaque=self, carte=cible, effet=effet)
                    effet_applique_sur.add(cible)
                    
                if test_crit:
                    self.declencher_evt_cible(cible, TypeEvenement.EFFET_CRITIQUE, attaque=self, carte=cible, effet=effet)
                    self.appliquer_effets_critiques(cible)

        self.carte.joueur.jeu.gestion_evt.declencher(TypeEvenement.APRES_ATTAQUE, attaque=self, attaque_rate=attaque_rate)

    def appliquer_effets_critiques(self, carte_cible: Optional["Carte"] = None) -> None:

        for effet in self.effets_critiques:
            cartes_cible = [carte_cible] if effet.cible_necessaire else effet.cartes_cibles(effet.cible)
            effet_copie = effet

            for cible in cartes_cible:
                if effet.test_cible(cible, effet.cible):
                    print(f"✨ Effet critique appliqué {'sur ' + cible.nom + ' ' if cible else ''}: {effet_copie.nom}")
                    effet_copie.appliquer(cible)
                    effet_copie = copy.deepcopy(effet)
                    effet_copie.attaque = self

    def attaquer(self, carte_cible: Optional["Carte"] = None) -> None:

        if not self.test_recharge():
            print(f"❌ {self.nom} est en recharge pour {self.recharge_actuelle} tour(s)")
            return 

        print(f"🚀 {self.carte.nom} attaque {carte_cible.nom + ' ' if carte_cible else ''}avec {self.nom}")

        self.appliquer_effets(carte_cible)

        self.fin_attaque()

        
            