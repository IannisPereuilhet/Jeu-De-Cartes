import random
import numpy as np
from enum import Enum, auto
from typing import List, Optional, Any, Dict, Union, Callable, TYPE_CHECKING, Literal, Tuple
import copy
from abc import ABC, abstractmethod
import os
import importlib

if TYPE_CHECKING:
    from src.carte import Carte
    from src.attaque import Attaque



carte_fumee = "❔❔❔❔❔"

class Element(Enum):
    FEU = auto()
    NATURE = auto()
    EAU = auto()
    TERRE = auto()
    LUMIERE = auto()
    OMBRE = auto()
    MULTI = auto()
    ALEATOIRE = auto()
    PRECEDENT = auto()
    JOUEUR = auto()
    CARTE = auto()
    AUCUN = auto()
    
    @classmethod
    def liste_elements(self):
        return [e for e in self if e in {self.FEU, self.NATURE, self.EAU, self.TERRE, self.LUMIERE, self.OMBRE}]
    
    @classmethod
    def aleatoire(self):
        return random.choice(self.liste_elements())
    
class TypeCible(Enum):
    UNE_CARTE = auto()
    UNE_CARTE_ALLIEE = auto()
    UNE_CARTE_ENNEMIE = auto()
    TOUS_LES_ENNEMIS = auto()
    TOUS_LES_ALLIES = auto()
    ALEATOIRE_ENNEMI = auto()
    ALEATOIRE_ALLIE = auto()
    ALEATOIRE_TOUTES_LES_CARTES = auto()
    TOUTES_LES_CARTES = auto()
    TOUTES_LES_CARTES_SAUF_SOI_MEME = auto()
    SOI_MEME = auto()
    AUCUNE = auto()
    ADVERSAIRE = auto()
    JOUEUR = auto()
    TOUS_LES_JOUEURS = auto()
    ATTAQUE = auto()

class TypeCalcul(Enum):
    CLASSIQUE = auto()
    PV_MAX = auto()
    PV_BAS = auto()
    MULTIPLICATEUR_ELEMENT = auto()

class TypeEvenement(Enum):
    DEBUT_JEU = auto()
    DEBUT_TOUR = auto()
    CHOIX_ATTAQUE = auto()
    AVANT_ATTAQUE = auto()
    AVANT_EFFET = auto()
    CALCUL_BONUS = auto()
    BONUS_ELEMENT = auto()
    APRES_SOIN = auto()
    APRES_DEGATS = auto()
    CARTE_MORTE = auto()
    APRES_UN_EFFET = auto()
    APRES_EFFET = auto()
    EFFET_CRITIQUE = auto()
    APRES_ATTAQUE = auto()
    FIN_TOUR = auto()

class TypeRarete(Enum):
    COMMUNE = auto()
    RARE = auto()
    EPIQUE = auto()
    LEGENDAIRE = auto()
    MYTHIQUE = auto()

def verifier_cartes(cartes: List["Carte"]) -> None:
    numeros = [carte.numero for carte in cartes]
    numeros_uniques = set(numeros)

    if len(numeros) != len(numeros_uniques):
        print("⚠️  Doublons détectés :")
        deja_vus = {}
        for carte in cartes:
            if carte.numero in deja_vus:
                print(f" - Numéro {carte.numero} : {deja_vus[carte.numero]} et {carte.nom}")
            else:
                deja_vus[carte.numero] = carte.nom
    # else:
    #     print("Aucun doublon détecté")

    if numeros:
        min_num, max_num = min(numeros), max(numeros)
        manquants = sorted(set(range(min_num, max_num + 1)) - numeros_uniques)
        if manquants:
            print("⚠️  Numéros manquants : " + ", ".join(str(n) for n in manquants))
        # else:
        #     print("Aucun numéro manquant")
    else:
        print("⚠️  Aucun numéro de carte trouvé")

def charger_attaques(dossier: str = "data.attaques") -> List["Attaque"]:
    attaques = []
    chemin_racine = os.path.join(*dossier.split("."))
    nombre_attaques = 0

    for element in os.listdir(chemin_racine):
        chemin_element = os.path.join(chemin_racine, element)
        if os.path.isdir(chemin_element) and not element.startswith("__"):
            for fichier in os.listdir(chemin_element):
                if fichier.endswith(".py") and not fichier.startswith("__"):
                    
                    nombre_attaques += 1
                    nom_fonction = fichier[:-3]
                    nom_module = f"{dossier}.{element}.{nom_fonction}"
                    module = importlib.import_module(nom_module)

                    if hasattr(module, nom_fonction):
                        attaque = getattr(module, nom_fonction)()
                        attaques.append(attaque)
                    else:
                        print(f"⚠️  Avertissement : {nom_module} ne contient pas de fonction '{nom_fonction}'")

    print(f"Nombre d'attaques chargées : {len(attaques)}/{nombre_attaques}")
    return attaques

def charger_cartes(dossier: str = "data.cartes") -> List["Carte"]:
    cartes = []
    chemin_racine = os.path.join(*dossier.split("."))
    nombre_cartes = 0

    for element in os.listdir(chemin_racine):
        chemin_element = os.path.join(chemin_racine, element)
        if os.path.isdir(chemin_element) and not element.startswith("__"):
            for fichier in os.listdir(chemin_element):
                if fichier.endswith(".py") and not fichier.startswith("__"):

                    nombre_cartes += 1
                    nom_fonction = fichier[:-3]
                    nom_module = f"{dossier}.{element}.{nom_fonction}"
                    module = importlib.import_module(nom_module)

                    if hasattr(module, nom_fonction):
                        carte = getattr(module, nom_fonction)()
                        cartes.append(carte)
                    else:
                        print(f"⚠️  Avertissement : {nom_module} ne contient pas de fonction '{nom_fonction}'")

    cartes.sort(key=lambda carte: carte.numero)

    nombre_total = 265

    print(f"Nombre de cartes chargées : {len(cartes)}/{nombre_cartes} - Objectif complété à {len(cartes) / nombre_total * 100:.2f}%")
    
    def affichage_carte(carte):
        print(f"\t- {carte.nom} (n°{carte.numero})")

    n = 10
    x = 0.8

    if len(cartes) <= n:
        for carte in cartes:
            affichage_carte(carte)
    else:
        for carte in cartes[:round((1-x)*n)]:
            affichage_carte(carte)
        for _ in range(3):
            print("\t\t   ·")
        for carte in cartes[-round(x*n):]:
            affichage_carte(carte)

    print("")
    verifier_cartes(cartes)

    return cartes