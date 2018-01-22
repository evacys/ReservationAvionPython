'''
Created on 6 avr. 2016

@author: eleve
'''
class Aeroport(object):
    def __init__(self,identifiant,nom,ville,lat,long):
        """
        Constructeur de la classe Aeroport
        
        Parametres:
        ville (objet de la classe Ville)
        lat = latitude (float)
        long = longitude (float)
        """
        self.id = identifiant
        self.nom = nom
        self.ville = ville
        self.lat = lat
        self.long = long
        
    def __str__(self):
        return self.nom
        
    def __repr__(self):
        return self.nom
