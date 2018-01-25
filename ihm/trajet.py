# -*- coding: utf-8 -*-

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')

import numpy as np
import datetime 
import fonction.conversion_fuseau as cf
import fonction.Algo_Dijkstra as ad
import fonction.Trouver_trajet as tt
from fonction.Recapitulatifs import *
from ihm.interaction import choisir
#date=datetime.datetime(2016,6,6,10,35)

#Roissy-Charles-de-Gaulle, Tegel

def convert_date(date): # date à mettre en guillemet si fonction utilisée seule 
    """
    Permet de covertir une date donnée sous la for YYYY-MM-DD HH:MM en objet date time.
    
    test:
    >>> convert_date("2016-06-06 12:13")
    datetime.datetime(2016, 6, 6, 12, 13)
    """
    year = ''
    month = ''
    day = ''
    hour = ''
    minute = ''
    for y in range(4): # Lecture de la chaine de caractere que l'on convertit en format datetime
        year += date[y]
    year = str(year)
            
    if date[5]!=0:
        month += date[5]
        month += date[6]
    elif date[5] == 0: 
        month += date[6]
    month = str(month)
        
    if date[8] != 0:
        day += date[8]
        day += date[9]
    elif date[8] == 0:
            day += date[9]
    day = str(day)
            
    if date[11] != 0:
        hour += date[11]
        hour += date[12]
    elif date[11] == 0:
        hour += date[12]
    hour = str(hour)

    if date[14] != 0:
        minute += date[14]
        minute += date[15]
    elif date[14] == 0:
        minute += date[15]
    minute = str(minute)
    
    date = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
    return date

def verif_date(date): # Date a mettre entre guillemet
    """ 
    Fonction qui vérifie que la date rentree est valide.
    
    Test:
    >>> verif_date('2016-06-06 20:00')
    True
    >>> verif_date('2016-06-06 20-00')
    False
    >>> verif_date('2016:06:06 20:00')
    False
    >>> verif_date('2016-06-06 ')
    False
    >>> verif_date('2016-06-06 2a:00')
    False
    >>> verif_date('2016-06-06 30:00')
    False
    >>> verif_date('2016-13-06 20:00')
    False
    """
    valide = True
    if len(date)!=16:
        valide=False
    elif date[4] != '-' or date[7] != '-' or date[10] != ' ' or date[13] != ':' :
        valide = False
    elif date[0] not in ['0','1','2','3','4','5','6','7','8','9'] or date[1] not in ['0','1','2','3','4','5','6','7','8','9'] or date[2] not in ['0','1','2','3','4','5','6','7','8','9'] or date[3] not in ['0','1','2','3','4','5','6','7','8','9'] or date[5] not in ['0','1'] or date[6] not in ['0','1','2','3','4','5','6','7','8','9'] or date[8] not in ['0','1','2','3'] or date[9] not in ['0','1','2','3','4','5','6','7','8','9'] or date[11] not in ['0','1','2'] or date[12] not in ['0','1','2','3','4','5','6','7','8','9'] or date[14] not in ['0','1','2','3','4','5'] or date[15] not in ['0','1','2','3','4','5','6','7','8','9']:
        valide = False
    elif date[5]=='1' and date[6] not in ['0','1','2']:
        valide =False
    elif date[8]=='3' and date[9] not in ['0','1']:
        valide=False
    elif date[11]=='2' and date[12] not in ['0','1','2','3']:
        valide=False
    else:
        valide = True
    return(valide)
        
def trouve_trajet(aeroports,villes,vols):
    """
    Fonction qui renvoie le trajet reliant aeroDep et aeroAr
    
    param:
    aeroDep = aeroport de depart
    aeroAr = aeroport d'arrivee
    dateDep = jour et heure à partir desquels on cherche des vols
    """
    villeDep=choisir(villes,"Voici la liste des villes desservies par la compagnie","Ville de départ: ")
    aero_villeDep=[]
    for aero in aeroports:
        if aero.ville==villeDep:
            aero_villeDep.append(aero)
    aeroDep =choisir(aero_villeDep,"Voici les aéroports que la compagnie dessert dans cette ville:","Lequel préférez vous? ")
    
    villeAr=choisir(villes,"Voici la liste des villes desservies par la compagnie","Ville d'arrivée: ")
    aero_villeAr=[]
    for aero in aeroports:
        if aero.ville==villeAr:
            aero_villeAr.append(aero)
    aeroAr =choisir(aero_villeAr,"Voici les aéroports que la compagnie dessert dans cette ville:","Lequel préférez vous? ")
    
    dateDep = input('Date de depart (YYYY-MM-DD hh:mm):')
    valide = verif_date(dateDep)
    while valide == False:
        print('La date rentrée est non valide')
        dateDep = input('date de depart (YYYY-MM-DD hh:mm):')
        valide = verif_date(dateDep)

    date = convert_date(dateDep) # Ne pas mettre de guillemets !!

    sif = tt.sif_poids(aeroDep,aeroAr,date,villes,vols)
    print('Nous vous proposons les vols suivants')
    chemin, vol = ad.dijkstra(str(aeroDep.nom),str(aeroAr.nom),sif)
    print(chemin,vol) # vol = liste des vols associés aux tronçons du chemin
    recapVol_pour_trajet(vols,vol)
    return(vol)

    
    