'''
Created on 6 avr. 2016

@author: eleve
'''

class Passager(object):
    def __init__(self, numRes,nom,prenom,mail):
        """ 
        Constructeur de la classe Passager
        
        param:
        numRes = numéro de reservation
        """
        self.numRes = numRes
        self.nom = nom
        self.prenom = prenom
        self.mail = mail

    def __str__(self):
        return str(self.numRes.id)
        
    def __repr__(self):
        return str(self.numRes.id)