# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:59:04 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
import fonction.Ajouter_passager as ap
from interaction import choisir

def Ajouter_un_passager(vols,passagers,reservations,chemin_bdd):
    '''
    Permet à un utilisateur d'ajouter un passager.
    '''
    print('Veuillez remplir les informations suivantes: ')
    nom=input('Nom: ')
    prenom=input('Prenom: ')
    mail=input('Adresse e-mail: ')
    #Vérification de la validité de l'adresse mail
    valide=Verif_mail(mail)                      
    while valide==False:
        print('Adresse non valide')
        mail=input('Adresse e-mail: ')
        valide=Verif_mail(mail)
    classe_possible=['Economique','Premiere','Business']
    classe=choisir(classe_possible,'Voici les classes possibles:','La quelle désirez vous? ')
    Nbvol=int(input('Combien le passager désire t il prendre de vol? '))
    liste_vols=[]
    for vo in range (1,Nbvol+1):
        if vo==1:
            num_vol=input('Numero du 1er vol: ')
        else:
            num_vol=input('Numero du {}ieme vol: '.format(vo))
        trouve=False
        cpt=0
        while trouve==False and vo<len(vols):
            if vols[cpt].num==num_vol:
                liste_vols.append(vols[cpt])
                trouve=True
            cpt+=1
            
        while not trouve:
            print("Numero non valide")
            if vo==1:
                num_vol=input('Numero du 1er vol: ')
            else:
                num_vol=input('Numero du {}ieme vol: '.format(vo))
                trouve=False
                cpt=0
                while trouve==False and vo<len(vols):
                    if vols[cpt].num==num_vol:
                        liste_vols.append(vols[cpt])
                        trouve=True
                        cpt+=1
    last_passenger=reservations[-1].id
    (reservations,passagers)=ap.ajouter_passager(nom, prenom, mail, liste_vols, classe, passagers, reservations, chemin_bdd)
    if last_passenger!=reservations[-1].id:
        print("\nVoici le numéro de réservation pour ce passager: {}".format(reservations[-1].id))
        return "\nL'ajout à bien été effectué, merci!"
    else:
        return("L'un des vols est complet.")
        
        
def Ajouter_un_passager_sur_certain_vol_donnés(liste_vols,vols,passagers,reservations,chemin_bdd):
    '''
    Permet à un utilisateur d'ahjouter un passager sur les vols de la liste_vols.
    '''
    print('Veuillez remplir les informations suivantes: ')
    nom=input('Nom: ')
    prenom=input('Prenom: ')
    mail=input('Adresse e-mail: ')
    classe_possible=['Premiere','Economique','Business']
    classe=choisir(classe_possible,'Voici les classes possibles:','La quelle désirez vous? ')
    (reservations,passagers)=ap.ajouter_passager(nom, prenom, mail, liste_vols, classe, passagers, reservations, chemin_bdd)
    print("\nVoici le numéro de réservation pour ce passager: {}".format(reservations[-1].id))
    return "L'ajout à bien été effectué, merci!"
    
    
def Verif_mail(mail):
    """
    Permet la verification d'une addresse mail.
    
    Entree:
    mail: type str: adresse mail à verifier
    
    Sortie:
    valide: type booleen
    
    Test:
    >>> Verif_mail('i.dg@gmail.com')
    True
    >>> Verif_mail('i.dg')
    False
    >>> Verif_mail('i.dg@gmail')
    False
    >>> Verif_mail('idg@.com')
    False
    >>> Verif_mail('huy@hadzu@ui.com')
    False
    >>> Verif_mail('deh@@ui.com')
    False
    """
    arrobaz=False
    point=False
    valide=False
    for lettre in range(len(mail)):
        if arrobaz==False:
            if mail[lettre]=='@':
                arrobaz=True
        elif arrobaz and not point:
            if mail[lettre]=='@':
                return(False)
            else:
                if mail[lettre-1]!='@':
                    if mail[lettre]=='.':
                        point=True
                        valide=True
            
        elif arrobaz and point:
            if mail[lettre]=='@':
                valide=False
    return valide