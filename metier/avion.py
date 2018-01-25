'''
Created on 6 avr. 2016

@author: eva
'''
import sys

import fonction.conversion_fuseau as cf
import datetime

class Avion(object):
    def __init__(self,id,capaciteMax,autonoMax):
        """ 
        Constructeur de la classe Avion
        """
        self.id = id
        self.capacite = capaciteMax # Nombre de passagers que peut acceuillir l'avion
        self.autono = autonoMax # autonomie de l'avion en km
        
    def localisation(self,date,vols,villes): 
        """
        Fonction qui permet de savoir où se trouve l'avion à une date et à une heure donnée, c'est-à-dire dans quel aéroport
        
        Entree:
        date: type datetime en en Greenwitch
        vols: liste de tous les vols de la compagnie
        villes: liste contenant toutes les villes desservies par des aeroports
        
        Sortie:
        localis: type objet aeroport: aeroport dans lequel l'avion
                ou type str :'L'avion est vol entre Aeroport1 et Aerport2'
        """  
        vo=0
        date_loc=datetime.datetime(1,1,1)   # date_loc contient la date à la quelle l'avion arrive à la localisation
        while vo<len(vols) and date_loc==datetime.datetime(1,1,1):
            if vols[vo].id_avion.id==self.id:
                localis=vols[vo].aeroAr
                date_loc=date_darrive_green(vols[vo],villes)
            vo+=1
        
        if date<date_loc:
            localis="L'avion est en vol entre {} et {}".format(vols[vo-1].aeroDep,vols[vo-1].aeroAr) #vo-1 car on avait incrementer vo de +1 à la fin du dernier passage dans la boucle while 
        else: 
            while date_loc<=date and vo<len(vols):
                if vols[vo].id_avion==self.id:
                    date_loc=date_darrive_green(vols[vo],villes)
                    if date_loc<=date:
                        localis=vo.aeroAr
                    else:
                        localis="L'avion est en vol entre {} et {}".format(vols[vo-1].aeroDep,vols[vo-1].aeroAr)   
                vo+=1
        return localis
        
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id
        

def date_darrive_green(vol,villes):
    '''
    Retourne la date date d'arrivee du vol en heure Greenwitch
    
    Entree:
    vol: tyoe objet vol
    villes: liste contenant toutes les villes desservies par des aeroports
    
    Sortie:
    dateAr_green: type datetime : date d'arrivee en Greenwitch
    '''
    dateDep_green=cf.localToGreen(vol.dateDep,vol.aeroDep.ville.decalage_fus)
    dateAr_green=dateDep_green+vol.duree
    return dateAr_green
