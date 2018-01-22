# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:55:34 2016

@author: Iris
"""
import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')

import fonction.chargement_classes as cc
from bdd.creation_bdd import creer_bdd
from ihm.interaction import choisir

from ihm.Ajout_passager import Ajouter_un_passager,Ajouter_un_passager_sur_certain_vol_donnés
from ihm.Supprimer_passager import Supprimer_un_passager
from ihm.Choix_avion import Choisir_un_avion
from fonction.Recapitulatifs import *
from ihm.visualisation import visualisation
from ihm.trajet import trouve_trajet



chemin_bdd=r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet\Icarus_bdd1.db'
#creer_bdd(chemin_bdd)
if __name__=="__main__":
    
    (avions, villes, passagers, reservations, vols, aeroports, compagnies)=cc.chargmt_classes(chemin_bdd)
    
    print("\nBIENVENUE DANS L'APPLICATION PAPER PLAN")
    appli_ouverte=True
    while appli_ouverte==True:
        fonctionalitees=["Ajouter un passager","Supprimer un passager","Recapitulatif d'un passager","Recapitulatif d'un vol","Attribuer un avion à un vol","Trouver un trajet entre deux aéroports","Tracer la carte des vols sur une periode","Fermer l'application"]
        volontee=choisir(fonctionalitees,"\nVoici la liste des fonctionalitées :","Que désirez-vous faire? ")
        if volontee=="Ajouter un passager":
            print(Ajouter_un_passager(vols,passagers,reservations,chemin_bdd))
        elif volontee=="Supprimer un passager":
            print(Supprimer_un_passager(passagers,reservations,chemin_bdd))
        elif volontee=="Recapitulatif d'un passager":
            print(recapPassager(passagers))
        elif volontee=="Recapitulatif d'un vol":
            print(recapVol(vols,reservations))
        elif volontee=="Attribuer un avion à un vol":
            print(Choisir_un_avion(vols,avions,villes,reservations,chemin_bdd))
        elif volontee== "Trouver un trajet entre deux aéroports":
            liste_vols=trouve_trajet(aeroports,villes,vols)
            if liste_vols!=[]:
                possibilite=["Oui","Non"]
                suite=choisir(possibilite,"Voulez vous inscrire un passager sur ce trajet? ")
                if suite=="Oui":
                    print(Ajouter_un_passager_sur_certain_vol_donnés(liste_vols,vols,passagers,reservations,chemin_bdd))
            else:
                print("Désolée le trajet indiqué n'est pas réalisable")
        elif volontee=="Tracer la carte des vols sur une periode":
            print(visualisation(vols))
        elif volontee=="Fermer l'application":
            appli_ouverte=False
    
    print("Paper Plan vous dit merci et à bientôt!")
    print("L'application est fermée, presser F5 pour l'ouvrir.")
        
    
    
    
    