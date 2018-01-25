# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:25:35 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
from bdd.acces_bdd import executer_requete, ouvrir_connexion, valider_modif, fermer_db

def supprimer_passager(passager, chemin_bdd, passagers, reservations):
    '''
    Permet  de suprimer des vols un passager. La suppression se fait dans la base de donnée et dans la liste passagers.
    
    Entrée:
    passager : type objet passager
    chemin_bdd : chemin de la base de donnee
    passagers : liste des objets passager
    reservations : liste des objets reservation
    
    Sortie:
    passagers : liste des objets passager dans la quelle on a supprime le passager
    reservations : liste des objets reservation dans la quelle on a supprime la reservation
    
    '''
    (base,curseur)=ouvrir_connexion(chemin_bdd)
    
    requete=''' delete from Passager where num_res={}'''.format(str(passager.numRes.id))
    executer_requete(curseur,requete) #on a suprimer le passager de la base de donnée
    requete=''' delete from Reservation where id={}'''.format( str(passager))
    executer_requete(curseur,requete)
    
    pos_passager=passagers.index(passager) # pos_passager contient l'indice de la position du passager dans la liste passagers
    passagers.pop(pos_passager)
    pos_reservation=reservations.index(passager.numRes) # pos_reservation contient l'indice de la position de la reservation dans la liste resrvations
    reservations.pop(pos_reservation)
    
    #On valide les modifications
    valider_modif(base)
    #on ferme la bdd
    fermer_db(base,curseur)
    
    return (passagers,reservations)
    

