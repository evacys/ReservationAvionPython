# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:50:07 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
import fonction.Choisir_avion as ca
from bdd.acces_bdd import executer_requete, ouvrir_connexion, valider_modif, fermer_db
from ihm.interaction import entrer_vol

def Choisir_un_avion(vols,avions,villes,reservations, chemin_bdd):
    """
    Permet à l'utilisateur de se selectionner un avion pour un vol donné.
    """
    vol=entrer_vol(vols)
    
    (vols,modification)=ca.choix_manuel_avion(vol, vols, avions, villes, reservations)
    
    if modification:
        (base,curseur)=ouvrir_connexion(chemin_bdd)
    
        requete=""" Update Vol set id_avion='{}' where id='{}'""".format(vol.id_avion.id,vol.num)
        executer_requete(curseur,requete)   # Il faut enregistrer la modification dans la base de donnée
        #On valide les modifications
        valider_modif(base)
        #on ferme la bdd
        fermer_db(base,curseur)
    
    return( "Opération terminée")
    

