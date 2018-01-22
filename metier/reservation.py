'''
Created on 6 avr. 2016

@author: eleve
'''

class Reservation(object):
    def __init__(self,idRes,liste_vols, classe):
        """
        Constructeur de la classe Reservation
        
        param:
        idRes = identifiant de la réservation
        classe = economique ou affaire
        numVol = numéro du vol
        """
        self.id = idRes
        self.classe = classe
        self.liste_vols = liste_vols

    def __str__(self):
        return self.id
    
    def __repr__(self):
        return str(self.id)