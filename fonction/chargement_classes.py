# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:58:36 2016

@author: Iris
"""
import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
from bdd.acces_bdd import executer_requete, ouvrir_connexion, fermer_db

from metier.aeroport import Aeroport
from metier.ville import Ville
from metier.avion import Avion
from metier.vol import Vol
from metier.compagnie import Compagnie
from metier.passager import Passager
from metier.reservation import Reservation

import datetime

chemin_bdd=r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet\Icarus_bdd.db'

def chargmt_classes(chemin_bdd):    
    
    (base,curseur)=ouvrir_connexion(chemin_bdd)
    
    #Remplissage de l'objet compagnie
    compagnies=[]
    for comp in executer_requete(curseur, "select * from Compagnie"):
        id_comp=comp[0]
        nom=comp[1]
        compagnies.append(Compagnie(id_comp,nom))       
        
    #Remplissage des objets Ville
    villes=[]
    for vi in executer_requete(curseur, "select * from Ville"):
        id_ville=vi[0]
        nom_ville=vi[1]
        pays=vi[2]
        decalage_fus=vi[3]
        villes.append(Ville(nom_ville,id_ville,pays,decalage_fus))
        
    #Remplissage des objets Aeroport 
    aeroports=[]
    for aero in executer_requete(curseur, "select * from Aeroport"):
        id_aero=aero[0]
        nom_aero=aero[1]
        id_ville_aero=aero[2]
        #Recherche de l'objet ville correspondant à l'identifiant de la ville donnée dans les attributs de l'aeroport
        trouve=False
        vi=0
        while trouve==False and vi<len(villes):
            if villes[vi].id==id_ville_aero:
                ville_aero=villes[vi] 
                trouve=True
            vi+=1
        lat_aero=float(aero[3])
        long_aero=float(aero[4])
        aeroports.append(Aeroport(id_aero,nom_aero,ville_aero,lat_aero,long_aero))
        
    #Remplissage des objets Avion
    avions=[]
    for av in executer_requete(curseur, "select * from Avion"):
        id_avion=av[0]
        capacitemax=av[1]
        autonomax=av[2]
        avions.append(Avion(id_avion,capacitemax,autonomax))
        
    #Remplissage des objets Vol
    vols=[]
    for vol in executer_requete(curseur, "select * from Vol"):
        
        numero_de_vol=str(vol[0])
        
        id_aero_dep=vol[1]
        #On recupere l'objet aeroport correspondant
        trouve=False
        ae=0
        while trouve==False and ae<len(aeroports):
            if aeroports[ae].id==id_aero_dep:
                aero_dep=aeroports[ae] 
                trouve=True
            ae+=1
            
        id_aero_ar=vol[2]
        trouve=False
        ae=0
        while trouve==False and ae<len(aeroports):
            if aeroports[ae].id==id_aero_ar:
                aero_ar=aeroports[ae] 
                trouve=True
            ae+=1  
            
        date_depart=vol[3]
        date_depart=date_depart.split(' ')
        # convertion de chaue entier de date_depart en type entier
        for i in range (len(date_depart)):
            if date_depart[i]!='':
                date_depart[i]=int(date_depart[i])
        #convertion de la chaine de caractere représentant la date en un objet de type date de la classe datetime
        date=datetime.datetime(date_depart[2],date_depart[1],date_depart[0],date_depart[3],date_depart[4])
        id_av=vol[4]
        if id_av!=None:        #Si un avion a deja ete attribué pour ce vol
            trouve=False
            av=0
            while trouve==False and av<len(avions):
                if avions[av].id==id_av:
                    id_avion=avions[av] 
                    trouve=True
                av+=1
            vols.append(Vol(numero_de_vol,aero_dep,aero_ar,date,id_avion))
        else:
            vols.append(Vol(numero_de_vol,aero_dep,aero_ar,date))
    
    #Remplissage des objets Reservation
    reservations=[]
    for resa in executer_requete(curseur,"select * from Reservation"):
        num_res=resa[0]
        l_vol=resa[1]
        l_vol=l_vol.split(', ')
        liste_vols=[]
        for vol in l_vol:
            trouve=False
            vo=0
            while trouve==False and vo<len(vols):
                if vols[vo].num==vol:
                    liste_vols.append(vols[vo])
                    trouve=True
                vo+=1 
        classe=resa[2]
        reservations.append(Reservation(num_res,liste_vols,classe))
    
    #Remplissage des objets Passager
    passagers=[]
    for passag in executer_requete(curseur, "select * from Passager"):
        numero_res=passag[0]
        trouve=False
        resa=0
        while trouve==False and resa<len(reservations):
            if reservations[resa].id==numero_res:
                num_res=reservations[resa] 
                trouve=True
            resa+=1  
                
        nom=passag[1]
        prenom=passag[2]
        adresse_mail=passag[3]
        passagers.append(Passager(num_res,nom,prenom,adresse_mail))
    
    #on ferme la bdd
    fermer_db(base,curseur)
        
    return(avions, villes, passagers, reservations, vols, aeroports, compagnies)