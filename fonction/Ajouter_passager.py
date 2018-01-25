# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:15:30 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
from bdd.acces_bdd import executer_requete, ouvrir_connexion, valider_modif, fermer_db
from metier.passager import Passager
from metier.reservation import Reservation

def ajouter_passager(nom, prenom, mail, liste_vols, classe, passagers, reservations, chemin_bdd):
    '''
    Permet d'ajouter un passager à la base de donner et aux liste d'objet.
    
    Entree:
    nom : type str : nom du client
    prenom : type str : prenom du client
    mail : type str : adresse email du client
    liste_vols : type list : liste des vols que le client veut empreinter
    classe : type str : classe desirée par le passager
    passagers : liste des objets passager
    reservations : liste des objets reservation
    curseur : surseur de la base de donnée dans la quelle faire l'ajout du passager
    
    Sortie: 
    passagers : liste des objets passager dans la quelle on a ajoute le passager
    reservations : liste des objets reservation dans la quelle on a ajoute la reservation
    '''
    (base,curseur)=ouvrir_connexion(chemin_bdd)
    
    if reservations!=[]:
        numRes=reservations[-1].id+1
    else:
        numRes=1
    
    complet=False
    for vol in liste_vols:
        Nb_passager=vol.nbPassager(reservations)
        if vol.id_avion!=None:      #On vérifie que si le vol à un avion attribué que celui n'est pas complet
            if Nb_passager>=vol.id_avion.capacite:
                complet=True
        if Nb_passager>=615:    #Meme s'il n'y a pas d'avion encore attribué alors dans tous les on ne pourra pas au dessus de 615 car c'est la capacité maximale du plus gros avion
            complet=True 
            
    if not complet:
        listeVols=str(liste_vols)
        listeVols = listeVols.replace('[','').replace(']', '')
        
        requete="""insert into Reservation (id, liste_vol, classe) values (?, ?, ?)"""
        executer_requete(curseur,requete, (numRes, listeVols, classe))
        requete="""insert into Passager (num_res, nom, prenom, mail) values (?, ?, ?, ?)"""
        executer_requete(curseur,requete, (numRes, nom, prenom, mail))
    
    
        reservations.append(Reservation(numRes,liste_vols,classe))
        passagers.append(Passager(reservations[-1], nom, prenom, mail))     # reservations[-1] reprend l'objet reservations qu'on vient d'ajouter 
        
        #On valide les modifications
        valider_modif(base)
        #on ferme la bdd
        fermer_db(base,curseur)
    return (reservations, passagers)