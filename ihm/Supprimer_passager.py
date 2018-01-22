# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:05:10 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
import fonction.Suppression_passager as sp
from ihm.interaction import entrer_numRes

def Supprimer_un_passager(passagers,reservations,chemin_bdd):
    """
    Permet à l'utilisateur de supprimer un passager.
    """
    passager=entrer_numRes(passagers) 
    (passagers,reservations)=sp.supprimer_passager(passager, chemin_bdd, passagers, reservations)
    return('La supression du passager a été effectuée')

          
