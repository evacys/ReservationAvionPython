# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:02:36 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
from ihm.interaction import choisir


def choix_manuel_avion(vol, vols, avions, villes, reservations):
    '''
    Permet le choix manuel d'un avion pour un vol donné
    
    Entrées:
    vol: type objet vol: vol sur lequel on ajouter l'avion
    vols : type list : liste de tous les vols
    avions: type list : liste de tous les avions
    villes: type list : liste de tous les villes
    reseservations: type list : liste de tous les reservations
    
    Sorties:
    vols : type list : liste mise à jour de tous les vols
    '''
    
    if vol.id_avion==None:
        nb_passager_vol=vol.nbPassager(reservations)
        liste_avion_dispo=recherche_avion_dispo(vol.aeroDep,vol.dateDep,nb_passager_vol,vol.distance,avions,vols,villes)
        msg='Le vol a à ce jour {} passagers inscrits.'.format(nb_passager_vol)
        print(msg)
        if len(liste_avion_dispo)!=0:
            choix=choisir(liste_avion_dispo,'Voici la liste des avions disponible pour ce vol.\n-800 : capacite: 615 passagers\n-1000 : capacite: 440 passagers\nAutre: capacite: 180 passagers\nQuel avion choisissez vous?')
            vol.id_avion=choix
            modification=True
        else:
            print("Il n'y a pas d'avion disponible à ce jour pour ce vol")
            modification=False
    else:
        print('Ce vol a déjà un avion attribué.')
        modification=False
    return (vols,modification)
    
def recherche_avion_dispo(aeroport,date,NbPassagers,distance,avions,vols,villes):
    '''
    Recherche de tous les avions disponible à un aeroport à une date pour un vol. La liste sortie ne contient que les aviosn possibles pour le vols, c'est à dire par rapport à la capacité et à l'autonomie maximale.
    
    Entrées:
    aeroport : type objet aeroport
    date : type datetime.datetime: date à la quelle on veut savoir s'il y a des avions disponible
    NbPassagers: type entier: nombre de passagers deja inscrit sur le vol
    distance: type float : distance du vol 
    avions: type list : liste de tous les avions
    vols : type list : liste de tous les vols
    villes: type list : liste de toutes les villes
    
    Sortie:
    avion_dispo: liste d'objet avion: liste des avions disponible
    '''
    avion_dispo=[]
    for av in avions:
        if distance<=av.autono:
            if NbPassagers<=av.capacite:
                if av.localisation(date,vols,villes)==aeroport:
                    reste_ici=avion_reste_aero(aeroport,av,vols,date)
                    if reste_ici:
                        avion_dispo.append(av)
    return avion_dispo

def avion_reste_aero(aeroport,avion,vols,date):
    '''
    Regarde lorsqu'un avion est à un aeroport, s'il va y rester ou s'il va prochainement décoller pour un prochain vol.
    
    Entrées:
    aeroport : type objet aeroport
    avion: type objet avion
    vols : type list : liste de tous les vols
    date : type datetime.datetime: date à la quelle on veut savoir s'il y a des avions disponible
    
    Sortie:
    reste: type booleen
    '''
    reste=True
    vo=0
    while reste and vo<len(vols):
        if vols[vo].id_avion==avion:
            if vols[vo].dateDep>=date:
                if vols[vo].aeroDep==aeroport:
                    reste=False
        vo+=1
    return(reste)