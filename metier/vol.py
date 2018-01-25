'''
Created on 6 avr. 2016

@author: eleve
'''

#import os
#os.chdir('C:\\Users\\Eva\\documents\\Cours_ENSG\\Projet_info\\projet\\projet\\metier')

import math as m
import numpy as np
import datetime



class Vol(object):
    def __init__(self,numero,aeroDep,aeroAr,dateDep,id_avion=None):
        """
        Constructeur de la classe Vol
        
        param:
        numero = numero de vol (str)
        aeroDep = aeroport de depart (objet)
        aeroAr = aeroport d'arrivee (objet)
        dateDep = date et heure de depart (au format datetime)
        """
        self.num = numero
        self.aeroDep = aeroDep
        self.aeroAr = aeroAr
        self.dateDep = dateDep
        self.id_avion = id_avion
    
    def __str__(self):
        return self.num
        
    def __repr__(self):# regarder le repr pour des int
        return self.num
    
    @property
    def distance(self,hautVol=5):
        """
        Fonction qui calcule la distance orthodromique en km entre 2 aéroports: aeroDep et aeroArr
        """
        lat1 = self.aeroDep.lat
        long1 = self.aeroDep.long
        lat2 = self.aeroAr.lat
        long2 = self.aeroAr.long
        dist = (6371+hautVol)*m.acos(m.cos(np.radians(lat1))*m.cos(np.radians(lat2))*m.cos(np.radians(long1-long2))+m.sin(np.radians(lat1))*m.sin(np.radians(lat2)))
        # On rajoute la hauteur de vol car distance plus grande lorsqu'on se trouve en hauteur
        return(dist)
    
    @property
    def duree(self,vitesse=900):
        """ 
        Fonction qui calcule la duree du vol en heure, elle retourne l'heure sous la datetime.timedelta
        
        param:
        vitesse = vitesse de vol que l'on suppose constante pendant tout le vol en km/h
        """
        d = self.distance
        t_h = d/vitesse
        heure=int(t_h)
        minu=(t_h-int(t_h))*60      # conversion des decimales en minutes
        if minu!=int(minu):         # On arrondit à la minute superieur
            minu=int(minu)+1
        duree=datetime.timedelta(hours=heure, minutes=minu)
        return (duree)
    
    def nbPassager(self,reservations):
        nb=0
        for re in reservations:
            for vo in re.liste_vols:
                if vo.num==self.num:
                    nb+=1
        return nb
        