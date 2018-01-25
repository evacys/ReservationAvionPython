# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:37:34 2016

@author: Iris
"""


def choisir(liste_choix, message_avant_liste = "", message_apres_liste=""):
    """
    Méthode de choix d'une action parmi une liste.
	
    :param liste_choix: liste des possibilités en entrée
    :param message_avant_liste: message à afficher pour aider l'utilisateur qui s'affichera avant la liste de proposition
    :param message_apres_liste: message à afficher pour aider l'utilisateur qui s'affichera apres la liste de proposition
    :return: choix
    """
    print(message_avant_liste)
    for i,elt in enumerate (liste_choix):
        print(i,elt)
    
    num=input(message_apres_liste)
    #num est une chaine il faut donc la convertir en entier     
    num=int(num)
    #verification que le numero est bien un indice de la liste
    while num>=len(liste_choix):
        print("Valeur non valide")
        num=input(message_apres_liste)
        num=int(num)
    return liste_choix[num]
    
    
def entrer_numRes(passagers):
    '''
    Permet d'entrer un numero de reservation, de verifier s'il est valide et de l'associer à un objet passager.
    
    Entree:
    passagers : liste des objets passager
    
    Sortie:
    passager: objet passager désiré par l'utilisateur
    
    '''
    numRes=int(input('Numero de reservation du passager (entier): '))
   
    
    trouve=False
    passag=0
    while trouve==False and passag<len(passagers):
        if passagers[passag].numRes.id==numRes:
            passager=passagers[passag] 
            trouve=True
        passag+=1 
        
    if not trouve :
        num_correct=False
        while not num_correct:
            print("Le numero indiqué n'existe pas")
            numRes=int(input('Numero de reservation du passager (entier): '))
            trouve=False
            passag=0
            while trouve==False and passag<len(passagers):
                if passagers[passag].numRes.id==numRes:
                    passager=passagers[passag] 
                    trouve=True
                    num_correct=True
                passag+=1 
    return passager
    

def entrer_vol(vols):
    '''
    Permet d'entrer un numero de vol, de verifier s'il est valide et de l'associer à un objet vol.
    
    Entree:
    vols : liste des objets vol
    
    Sortie:
    vol: objet vol désiré par l'utilisateur
    
    '''
    num_vol=input("Numero de vol (entier): ")
    trouve=False
    vo=0
    while trouve==False and vo<len(vols):
        if vols[vo].num==num_vol:
            vol=vols[vo]
            trouve=True
        vo+=1
            
    if not trouve :
        num_correct=False
        while not num_correct:
            print("Le numero indiqué n'existe pas")
            num_vol=int(input("Numero de vol (entier): "))
            trouve=False
            vo=0
            while trouve==False and vo<len(vols):
                if vols[vo].num==num_vol:
                    vol=vols[vo]
                    trouve=True
                vo+=1
    return vol