# -*- coding: utf-8 -*-

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')
#sys.path.append(r'C:\Users\Eva\Documents\Cours_ENSG\Projet_info\projet\projet')
import datetime
import numpy as np
import matplotlib.pyplot as plt
import math as m
import fonction.conversion_fuseau as cf
import pylab
import matplotlib.patches as mpatches


f=1/298.257222101
e= np.sqrt(2*f-f*f)
Xc=0
Yc=0
n=6378137

def selectVol(vols,dateDeb,dateFin):
    """
    Fonction qui va permettre de selectionner parmi les vols ceux qui s'effectuent entre la date de début, dateDeb et la date de fin, dateFin
    utilité: visualisation destinations desservies 
    param:

    vols = Liste des vols prévus par la compagnie
    dateDep et dateFin doivent etre rentres sous la forme "datetime.datetime(2016, 5, 7, 8, 30)" heure de Greenwich
    """
    vo = [] # On enregistre les vols compris dans la tanche horaire voulue dans une liste
    for i in range (len(vols)): # On parcourt toute la liste des vols
        decalage = vols[i].aeroDep.ville.decalage_fus  # On recupere le decalage par rapport au fuseau de Greenwich
        date = cf.localToGreen(vols[i].dateDep,decalage) # il faut convertir l'heure du vol (en heure locale de l'aeroDep) en heure de Greewich
        if dateDeb < date < dateFin:
            #vo.append(Vol(vols[i].num,vols[i].aeroDep,vols[i].aeroAr,vols[i].dateDep,vols[i].id_avion))
            vo.append(vols[i])
            #print(vols[i].aeroDep,'et',vols[i].aeroAr)
    return vo


def latitudeIso(phi):
    """ 
    Fonction qui permet de convertir une latitude phi en latitude isometrique
    
    >>> latitudeIso(m.pi/4)
    0.87663465341138258
    """
    L=m.log(m.tan((m.pi/4)+(phi/2)))-(e/2)*m.log((1+e*m.sin(phi))/(1-e*m.sin(phi)))
    return(L)
    
    
def lire(cheminFichier):
    """
    Fonction qui permet de lire le fihier dans la destination cheminFichier
    """
    fichier = open(cheminFichier,"r")
    ligne = fichier.readlines()
    return ligne
      
    
def mercator_plus_tous_les_vols(vols,dateDeb,dateFin,Xc=0,Yc=0,n=6378137,cheminFichier=r"C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\projet\ihm\coast.txt"):
    M1=[]
    M2=[]
    coord_dep = []
    coord_ar = []
    x = []
    y = []
    vo = selectVol(vols,dateDeb,dateFin)
    ligne=lire(cheminFichier)
    for i in range(len(ligne)):
        tab=ligne[i].split()
        lat=float(tab[0])
        long=float(tab[1])
        X= Xc + n*(m.pi*long)/180
        Y = Yc + n*latitudeIso((m.pi*lat)/180)
        M1.append(X)
        M2.append(Y)
    pylab.subplot(111, axisbg='#f2f2f2')
    plt.plot(M1,M2,color='grey')
    vo = selectVol(vols, dateDeb,dateFin)
    for t in range(len(vo)):
        x.append(Xc + n*(m.pi*vo[t].aeroDep.long)/180) # on recupere les coordonnees de tous les aeroports
        y.append(Yc +n*latitudeIso((m.pi*vo[t].aeroDep.lat)/180))
        x.append(Xc + n*(m.pi*vo[t].aeroAr.long)/180)
        y.append(Yc +n*latitudeIso((m.pi*vo[t].aeroAr.lat)/180))
        plt.plot(x,y,'bo')
        coord_dep.append((Xc + n*(m.pi*vo[t].aeroDep.long)/180,Yc +n*latitudeIso((m.pi*vo[t].aeroDep.lat)/180))) #on recupere les coordonnees des aero. dep
        coord_ar.append((Xc + n*(m.pi*vo[t].aeroAr.long)/180,Yc +n*latitudeIso((m.pi*vo[t].aeroAr.lat)/180))) #on recupere les coordonnees des aero. ar

    for s in range(len(coord_dep)):
        for u in range(len(coord_ar)):
            if coord_dep[s] == coord_ar[u] and coord_ar[s] == coord_dep[u]:
                Xp = [coord_dep[s][0],coord_ar[s][0]]
                Yp = [coord_dep[s][1],coord_ar[s][1]]
                plt.plot(Xp,Yp,'-',color='black',linewidth=0.4,label = "Vol double")
            else:
                Xp = [coord_dep[s][0],coord_ar[s][0]]
                Yp = [coord_dep[s][1],coord_ar[s][1]]
                plt.plot(Xp,Yp,'--',color='black',linewidth=0.3,label = "Vol simple")
    plt.title("Destinations désservies")
    plt.figtext(0.1, 0, '- - - Vols simples')
    plt.figtext(0.5, 0, '- Vols doubles')
    plt.axis([-2.3*10**7,2.3*10**7,-2.3*10**7,2*10**7])
    plt.show()

def mercator_plus_certains_vols(liste_vols,cheminFichier=r"C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\projet\ihm\coast.txt") :
    """
    Fonction qui permet de tracer sur une carte les vols contenus dans liste_vols
    """
    M1=[]
    M2=[]

    
    ligne=lire(cheminFichier)
    for i in range(len(ligne)):
        tab=ligne[i].split()
        lat=float(tab[0])
        long=float(tab[1])
        X= Xc + n*(m.pi*long)/180
        Y = Yc + n*latitudeIso((m.pi*lat)/180)
        M1.append(X)
        M2.append(Y)
    pylab.subplot(111, axisbg='#f2f2f2')
    plt.plot(M1,M2,color='grey')
    
    xmin=min(liste_vols[0].aeroDep.long,liste_vols[0].aeroAr.long)
    xmax=max(liste_vols[0].aeroDep.long,liste_vols[0].aeroAr.long)
    ymin=min(liste_vols[0].aeroDep.lat,liste_vols[0].aeroAr.lat)
    ymax=max(liste_vols[0].aeroDep.lat,liste_vols[0].aeroAr.lat)
    
    for t in range (len(liste_vols)):
        if t==0:#Lorsque t==0 alors c'est le premier vol du trjet le depart doit etre marqué d'une certaine couleur
            x=(Xc + n*(m.pi*liste_vols[t].aeroDep.long)/180) 
            y=(Yc +n*latitudeIso((m.pi*liste_vols[t].aeroDep.lat)/180))
            plt.plot(x,y,'bo',color='blue')
            
            if len(liste_vols)==1:
                x=(Xc + n*(m.pi*liste_vols[t].aeroAr.long)/180)
                y=(Yc +n*latitudeIso((m.pi*liste_vols[t].aeroAr.lat)/180))
                plt.plot(x,y,'bo', color='red')
            else:
                x=(Xc + n*(m.pi*liste_vols[t].aeroAr.long)/180)
                y=(Yc +n*latitudeIso((m.pi*liste_vols[t].aeroAr.lat)/180))
                plt.plot(x,y,'.', color='black')
                
        elif t==len(liste_vols)-1:#Lorsque c'est le dernier vol du trajet l'arrivée doit etre marqué d'une certaine couleur
             x=(Xc + n*(m.pi*liste_vols[t].aeroAr.long)/180)
             y=(Yc +n*latitudeIso((m.pi*liste_vols[t].aeroAr.lat)/180))
             plt.plot(x,y,'bo', color='red')
        else:#On marque toujours l'aeroport d'arrivée du vol car l'aeroport de départ a été marqué au tour précédent
             x=(Xc + n*(m.pi*liste_vols[t].aeroAr.long)/180)
             y=(Yc +n*latitudeIso((m.pi*liste_vols[t].aeroAr.lat)/180))
             plt.plot(x,y,'.', color='black')
            
    x=[]
    y=[]
        
    for vo in liste_vols:
        x.append(Xc + n*(m.pi*vo.aeroDep.long)/180)
        y.append(Yc +n*latitudeIso((m.pi*vo.aeroDep.lat)/180))
        x.append(Xc + n*(m.pi*vo.aeroAr.long)/180)
        y.append(Yc +n*latitudeIso((m.pi*vo.aeroAr.lat)/180))
        plt.plot(x,y,'-',color='black',linewidth=1)
        
        if xmin>min(vo.aeroDep.long,vo.aeroAr.long):
            xmin=min(vo.aeroDep.long,vo.aeroAr.long)
        if xmax<max(vo.aeroDep.long,vo.aeroAr.long):
            xmax=max(vo.aeroDep.long,vo.aeroAr.long)
        if ymin>min(vo.aeroDep.lat,vo.aeroAr.lat):
            ymin=min(vo.aeroDep.lat,vo.aeroAr.lat)
        if ymax<max(vo.aeroDep.lat,vo.aeroAr.lat):
            ymax=max(vo.aeroDep.lat,vo.aeroAr.lat)
    Xmin= Xc + n*(m.pi*xmin)/180
    Xmax=Xc + n*(m.pi*xmax)/180
    Ymin = Yc + n*latitudeIso((m.pi*ymin)/180)
    Ymax = Yc + n*latitudeIso((m.pi*ymax)/180)

    (xmil,xmal,ymil,ymal)=choix_zoom(Xmin,Xmax,Ymin,Ymax)

    plt.axis([xmil,xmal,ymil,ymal])
    plt.figtext(0.1, 0, 'o Départ',color='blue')
    plt.figtext(0.5, 0, 'o Arrivée',color='red')
    plt.show()
    

def choix_zoom(xmin,xmax,ymin,ymax):
    """
    Fonction permetant le choix d'un zoom adapter aux vols présents sur la carte.
    
    Entrées:
    xmin/xmax: x min/max des aeroports 
    ymin/ymax: y min/max des aeroports
    
    Sortie:
    xmil,xmal,ymil,ymal à appliququer pour avoir le bon zoom
    """
    #zoom monde
    xmil=-2.5*10**7*0.9
    xmal=2.5*10**7*0.9
    ymil=-2*10**7*0.99
    ymal=2*10**7*0.99
    #zoom europe
    if -0.3*10**7<=xmin<=10**7 and -0.3*10**7<=xmax<=10**7 and 0<=ymin<=1.5*10**7 and  0<=ymax<=1.5*10**7:
        xmil=xmil*0.2
        xmal=xmal*0.4
        ymil=ymil*0
        ymal=ymal*0.6
    
    #zoom Etats Unis
    elif -1.5*10**7<=xmin<=0 and -1.5*10**7<=xmax<=0 and 0<=ymin<=1*10**7 and  0<=ymax<=1*10**7:

        xmil=xmil*0.8
        xmal=xmal*(-0.2)
        ymil=ymil*0
        ymal=ymal*0.5
    
    #zoom atlantique
    elif -1.5*10**7<=xmin<=10**7 and -1.5*10**7<=xmax<=10**7 :
 
        xmil=xmil*0.5
        xmal=xmal*0.25
        ymil=ymil*0.4
        ymal=ymal*0.6
       
    #zoom Eurasie-Affrique-Océanie
    elif 0<=xmin and  0<=xmax :
        xmil=xmil*(0.2)
        xmal=xmal
        ymil=ymil*0.4
        ymal=ymal*0.6
        
    return (xmil,xmal,ymil,ymal)
    
    
#dateDeb = datetime.datetime(2016, 12, 30, 12, 00)
#dateFin = datetime.datetime(2016, 12, 30, 19, 50)
#mercator("coast.txt",Xc,Yc,n,vols,dateDeb,dateFin) 
#  
