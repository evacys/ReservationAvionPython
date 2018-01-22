# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:27:21 2016

@author: Iris
"""

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')

import time 
import numpy as np
import datetime 
import fonction.conversion_fuseau as cf

date=datetime.datetime(2016,6,6,20,35)

def sif_poids(aeroDep,aeroAr,date,villes,vols,delta=datetime.timedelta(hours=24)):
    """
    On recherche tous les trajets possibles dans les 24h suivantes de la date allant de aerodep à aeroar.
    Ces vols sont contenus dans une matrice à 4 colonnes, une ligne par vol. 
    
    Entree:
    aeroDep : objet aeroport
    aeroAr : objet aeroport
    date: objet date, date et heure desiree
    villes : liste des objets villes
    vols : liste des objets vols
    delta : type: timedelta: intervalle de temps pendant lequel on autorise le depart apres la date indiqué comme date desiree
    
    Sortie:
    sif : array (ligne: len(vol_a_insere),colonne:4)
    colonne 0 : Aeroport de depart
    colonne 1 : Aeroport d'arrivee
    colonne 2 : duree du trajet un heure decimale
    """
    #Conversion de l'heure selon l'heure Greenwich

    villeDep=aeroDep.ville       
    (date_deb_green,date_fin_green)=intervale_tps(delta,date,villeDep,villes)     # On va regarder dans les heures suivantes les vols partant de l'aeroport
    vol_trajet=[]
    for vo in vols:
        date_vol=vo.dateDep
        date_vol_green=cf.localToGreen(date_vol,villeDep.decalage_fus)
        if date_deb_green<=date_vol_green<=date_fin_green:      #On verifie que le vol est bien dans l'intervale de temps desiré par l'utilisateur
            aeroDepVol=vo.aeroDep
            if aeroDep==aeroDepVol: # On rentre dans la matrice sif au debut tous les vols qui partent de l'aeroport de depart dans le creneau de temps prevu
                vol_trajet.append(vo)

    arrive=False
    
    aeroCorres_Dep=[aeroDep]

    while arrive==False:        # On choisit que des qu'on a trouvé un vol qui arrive à l'aerport d'arrivee on coupe le programme
        ligne=0
        vol_correspondance=[]   # Remplissage d'une liste contenant tous les derniers vols ajoutes
        while arrive==False and ligne<len(vol_trajet):
            for aero in aeroCorres_Dep:
                if vol_trajet[ligne].aeroDep==aero:
                    if vol_trajet[ligne].aeroAr==aeroAr:        # Verification si on est arrivé à l'aeroport d'arrive
                        arrive=True
                    else:
                        
                        vol_correspondance.append(vol_trajet[ligne])
        
            ligne+=1  
        if arrive==False:
            aeroCorres_Dep=[]
            if len(vol_correspondance)!=0:
                for corres in vol_correspondance:
                    (vol_trajet,ajoute)=ajout_vol_a_partir_dune_correspondance(vol_trajet,corres,vols,villes,delta)
                                       
                    if ajoute:
                        aeroCorres_Dep.append(corres.aeroAr)
                
            else:       
                #S'il n'y a pas de correspondance et qu'on est toujours pas arrivé, 
                #cela signifie qu'il est impossible de joindre l'aeroport de depart à celui d'arrivée par cette compagnie
                print('ici')                
                arrive=True
                sif=remplir_sif(vol_trajet)
            

                
    sif=remplir_sif(vol_trajet)
    return sif

def intervale_tps(delta,date,villeDate,villes):
    '''
    Permet de donner l'intervale de temps c'est à dire [date;date+delta] le tout en heure Greenwich.
    
    Entree:
    delta : type : timedelta
    date : date au format datetime en fuseau local de la ville villeDate
    villeDate : objet ville dans laquelle est donné la date
    villes: liste d'objet villes
    
    Sortie:
    date_deb_green : objet datetime en greenwich de debut
    date_fin_green : objet datetime en greenwich de fin
    '''
    decalFus=villeDate.decalage_fus
    date_deb_green=cf.localToGreen(date,decalFus)      # date_green_deb contient la date Greenwich desiré par l'utilisateur 
    date_fin_green=date_deb_green+delta       
    return (date_deb_green,date_fin_green)

def ajout_vol_a_partir_dune_correspondance(vol_trajet,corres,vols,villes,delta):
    '''
    Permet d'ajouter à la liste vol_trajet tous les vols qui partent de la ville d'arrivee du vol precedent qui sont dans les horraires correspondant.
    On se debrouille aussi pour ne pas mettre un vol qui revient à laeroport precedent et pour choisir un vol dont le trajet n'a pas deja été fait (pour ne pas boucler indefiniment)
    
    Entree: 
    vol_trajet : liste des vols deja choisi
    corres: type objet vol: vol precedent
    vols: liste de tous les vols
    villes : liste de toutes les villes
    delta : type : timedelta
    
    Sortie:
    vol_trajet: liste des vols completee
    ajoute: type booleen: qui dit si oui ou non corres à été ajouté 
    '''
    ajoute=False
    vol_corres_dateAr=corres.dateDep+corres.duree   # On recupere l'heure d'arrivee du vol
    (vol_corres_dateAr_green,vol_corres_dateAr_green_fin)=intervale_tps(delta,vol_corres_dateAr,corres.aeroDep.ville,villes)
    for vo in vols:
        date_vol=vo.dateDep
        decal_ville_corres=vo.aeroDep.ville.decalage_fus    # Conversion en Greenwich
        date_vol_green=cf.localToGreen(date_vol,decal_ville_corres)
        if vol_corres_dateAr_green<=date_vol_green<=vol_corres_dateAr_green_fin:      # On verifie que le vol est bien dans les 24h suivantes de la demande de l'utilisateur
            aeroDepVol=vo.aeroDep
            if aeroDepVol==corres.aeroAr: # On regarde si l'aeroport de depart du vol correspondant à l'aéroport de correspondance
                res_trajet_deja_fait=trajet_deja_fait(vol_trajet,vo) # Retourne un booleen
                res_vol_retour=vol_retour(corres,vo)        # Retourne un booleen
                if res_trajet_deja_fait==False and res_vol_retour==False:
                    vol_trajet.append(vo)
                    ajoute=True
    return (vol_trajet,ajoute)

def trajet_deja_fait(vol_trajet,vol):
    '''
    Ce programme verifie si un trajet entre l'aeroport de depart et d'arrivee du vol a deja ete rentre dans la liste vol_trajet.
    Ce ne doit pas ere necessaireement le même vol mais simplement le meme trajet.
    
    Entree:
    vol_trajet : liste d'objet vol
    vol : objet vol a teste
    
    Sortie:
    Booleen 
    '''
    res=False
    vo=0
    while res==False and vo<len(vol_trajet):
        if vol_trajet[vo].aeroDep==vol.aeroDep and vol_trajet[vo].aeroAr==vol.aeroAr:
            res=True
        vo+=1
    return res
    
def vol_retour(vol1,vol2):
    '''
    Test si le vol2 est le retour du vol1 en tenant simplement compte des aeroports
    
    Entree:
    vol1 : objet vol
    vol2 : objet vol
    
    Sortie:
    Booleen
    '''
    if vol1.aeroDep==vol2.aeroAr and vol1.aeroAr==vol2.aeroDep:
        res=True
    else:
        res=False
    return res

def remplir_sif(vol_a_insere):
    '''
    Permet de remplir la matrice sif à partir de la liste de tous les vols à inserer dans cette matrice.
    
    Entree:
    vol_a_insere : liste d'objet vol
    
    Sortie:
    sif : array (ligne: len(vol_a_insere),colonne:3)
    colonne 0 : Aeroport de depart
    colonne 1 : Aeroport d'arrivee
    colonne 2 : duree du trajet un heure decimale
    '''
    if len(vol_a_insere)!=0:
        sif=np.array([[0,0,0,0]])
        for vol in vol_a_insere:
            dur=vol.duree
            dur=str(dur)
            dur=dur.split(':')
            tps_vol=int(dur[0])
            tps_vol+=float(dur[1])/60
            ligne=np.array([str(vol.aeroDep),str(vol.aeroAr),tps_vol,vol])
            sif=np.vstack((sif,ligne))
        sif=np.delete(sif,0,0)      # On supprime la premiere ligne de zero qu'on avait mis
    else:
        sif=np.array([])        # On retourne une matrice vide si aucun vol n'est a inserer
    return sif
        

