# -*- coding: utf-8 -*-

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
from fonction.conversion_fuseau import *
from ihm.interaction import entrer_vol, entrer_numRes
import fonction.tracer_carte as tc

def recapVol(vols,reservations):
    """ 
    Fonction qui à partir du numero de vol numero_de_vol renvoie le recapitulatif de ce dernier
    
    param:
    vols = liste des vols
    """
    vol = entrer_vol(vols)
    
    titre = "\nrecapitulatif de vol"
    titre = titre.upper().center(20)
    print(titre)
    print("\nNumero de vol: {0} \nVille de départ: {1} ({2}) \nAeroport de depart: {3} \nVille d'arrivée: {4} ({5}) \nAeroport d'arrivee: {6} \nAvion effectuant le vol: {7} \nNombre de passager inscrit pour le moment: {8}".format(vol.num, vol.aeroDep.ville, vol.aeroDep.ville.pays, vol.aeroDep, vol.aeroAr.ville, vol.aeroAr.ville.pays, vol.aeroAr, vol.id_avion, vol.nbPassager(reservations))) # On renvoie les informations relatives au vol
    print("\nVol prévu le:")
    print(vol.dateDep)
    print("Arrivée prévu le (heure locale):")
    print(greenToLocal(localToGreen(vol.dateDep,vol.aeroDep.ville.decalage_fus) +vol.duree,vol.aeroAr.ville.decalage_fus))
    print("Durée du vol: {}".format(vol.duree))
    L_vol=[]
    L_vol.append(vol)
    tc.mercator_plus_certains_vols(L_vol)
    return('------')

def recapVol_pour_trajet(vols,numero_de_vol):
    """ 
    Fonction qui à partir du numero de vol numero_de_vol renvoie le recapitulatif de ce dernier
    
    param:
    vols = liste des vols
    numero_de_vol = liste de vols dont on souhaite le recap
    """
    titre = "recapitulatif de vol"
    titre = titre.upper().center(20)
    print(titre)
    for i in range(len(numero_de_vol)):
        print("\nNumero de vol: {0} \nVille de départ: {1} ({2}) \nAeroport de depart: {3} \nVille d'arrivée: {4} ({5} \nAeroport d'arrivee: {6} \nAvion effectuant le vol: {7} ".format(numero_de_vol[i].num, numero_de_vol[i].aeroDep.ville,numero_de_vol[i].aeroDep.ville.pays, numero_de_vol[i].aeroDep, numero_de_vol[i].aeroAr.ville, numero_de_vol[i].aeroAr.ville.pays, numero_de_vol[i].aeroAr, numero_de_vol[i].id_avion)) # On renvoie les informations relatives au vol
        print("\nVol prévu le:")
        print(numero_de_vol[i].dateDep)
        print("Arrivée prévu le (heure locale):")
        print(greenToLocal(localToGreen(numero_de_vol[i].dateDep,numero_de_vol[i].aeroDep.ville.decalage_fus) +numero_de_vol[i].duree,numero_de_vol[i].aeroAr.ville.decalage_fus))
        print("Durée du vol: {}".format(numero_de_vol[i].duree))
    
    if len(numero_de_vol) > 1:
        print('\n')
        for t in range (len(numero_de_vol)-1):
            date = localToGreen(numero_de_vol[t].dateDep + numero_de_vol[t].duree,numero_de_vol[t].aeroDep.ville.decalage_fus)
            corres = localToGreen(numero_de_vol[t+1].dateDep,numero_de_vol[t+1].aeroDep.ville.decalage_fus) - date
            print("Entre le vol numero {0} et {1} vous avez {2} temps d'attente".format(numero_de_vol[t].num,numero_de_vol[t+1].num,corres))
    tc.mercator_plus_certains_vols(numero_de_vol)
    return('------')    
 
   
def recapPassager(passagers):
    """
    Fonction qui à partir du numero de reservation numero_de_resa d'un passager renvoie le recapitulatif de son vol 
    
    param:
    passagers = liste des passagers
    numero_de_resa = numero de reservation
    """ 
    passager =entrer_numRes(passagers)   
   
    n = len(passager.numRes.liste_vols)
    classe = passager.numRes.classe
    
    titre = "\nrecapitulatif de passager"
    titre = titre.upper().center(20)
    print(titre)
    print("\nNom: {}\nPrenom: {}\nAdresse mail: {}".format(passager.nom,passager.prenom,passager.mail))
    print("Numero de reservation: {0} \n\nVille de départ: {1} ({2})\nAeroport de depart: {3} \nVille d'arrivée: {4} ({5}) \nAeroport d'arrivee: {6} \nClasse: {7}".format(passager.numRes.id,passager.numRes.liste_vols[0].aeroDep.ville,passager.numRes.liste_vols[0].aeroDep.ville.pays,passager.numRes.liste_vols[0].aeroDep,passager.numRes.liste_vols[n-1].aeroAr.ville, passager.numRes.liste_vols[n-1].aeroAr.ville.pays, passager.numRes.liste_vols[n-1].aeroAr,classe)) 
    print('\nVos vols prévus sont les suivants:')
    for j in range (len(passager.numRes.liste_vols)):
        dateAr = greenToLocal(localToGreen(passager.numRes.liste_vols[j].dateDep,passager.numRes.liste_vols[j].aeroDep.ville.decalage_fus) + passager.numRes.liste_vols[j].duree,passager.numRes.liste_vols[j].aeroAr.ville.decalage_fus)
        print("\n{} - {}".format(passager.numRes.liste_vols[j].aeroDep,passager.numRes.liste_vols[j].aeroAr))
        print('Numero de vol: ',passager.numRes.liste_vols[j].num)
        print('Date de depart: ',passager.numRes.liste_vols[j].dateDep)
        print("Date d'arrivee: ",dateAr)
        print("Durée du vol: {}".format(passager.numRes.liste_vols[j].duree))
    if n > 1:
        print('\n')
        for t in range (n-1):
            date = localToGreen(passager.numRes.liste_vols[t].dateDep + passager.numRes.liste_vols[t].duree,passagers[0].numRes.liste_vols[t].aeroDep.ville.decalage_fus)
            corres = localToGreen(passager.numRes.liste_vols[t+1].dateDep,passager.numRes.liste_vols[t+1].aeroDep.ville.decalage_fus) - date
            print("Entre le vol numero {0} et {1} vous avez {2} temps d'attente".format(passager.numRes.liste_vols[t].num,passager.numRes.liste_vols[t+1].num,corres))
    
    tc.mercator_plus_certains_vols(passager.numRes.liste_vols)
    
    return('------')

    
        