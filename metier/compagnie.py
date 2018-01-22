'''
Created on 6 avr. 2016

@author: eleve
'''

class Compagnie(object):
    def __init__(self,nom,id_compagnie):
        """
        Constructeur de la classe Compagnie
        """
        self.nom = nom
        self.id=id_compagnie
        
    def attribAvion(self, numVol): # Fonction qui permet de déterminer l'avion effectuant le vol affecté à numVol
        pass

    def __str__(self):
        return self.nom
    
    def __repr__(self):
        return self.nom