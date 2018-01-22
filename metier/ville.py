'''
Created on 6 avr. 2016

@author: eleve
'''

class Ville(object):
    def __init__(self,nom,identifiant,pays,decalageFus):
        """ 
        Constructeur de la classe Ville
        
        param:
        decalageFus = Decalage par rapport au fuseau horaire de reference
        """
        self.nom = nom
        self.id = identifiant
        self.pays = pays
        self.decalage_fus = decalageFus

    def __str__(self):
        return self.nom
        
    def __repr__(self):
        return self.nom