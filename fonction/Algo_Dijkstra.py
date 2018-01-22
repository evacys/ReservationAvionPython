# -*- coding: utf-8 -*-

import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')

import numpy as np  
from fonction.Trouver_trajet import *
import datetime
   
#date = datetime.datetime(2016, 12, 30, 12, 00)
#sif = sif_poids(aeroports[0],aeroports[5],date,villes,vols)
#Si1 = 'OR Tambo'
#Sf = 'Cheremetievo'
#dijkstra(Si1,Sf,sif)

   
def fonc(liste,chaine):
    """
    Fonction qui cherche la presence de chaine dans liste.
    Elle renvoie True si chaine est présente et sa position dans liste, False sinon et -1 par défaut. 

    >>> liste = [('A',1),('B',2)]
    >>> fonc(liste,'A')
    (True, 0)
    >>> fonc(liste,'C')
    (False, -1)
    """
    t = 0
    p = -1
    present = False
    for i in range(len(liste)):
        if liste[t][0] == chaine:
            present = True
            p = t
        else:
            t+=1
    return (present,p)
    

def dijkstra(Si1,Sf,sif):
    """
    Fonction qui permet de trouver le plus court chemin entre le sommet innitial Si1 et le sommet final Sf
    
    param:
    Si1/ Sf = sommets initiaux/finaux
    sif = table SIF des sommets initiaux et finaux et des poids associé à chaque arc
    
    >>> sif = np.array([['E','A',3,10],['E','B',1,11],['A','C',2,12],['C','S',3,13],['B','D',5,14],['D','S',1,15],['B','C',3,16],['A','B',1,17],['D','C',1,18]])
    >>> Si1 = 'E'
    >>> Sf = 'S'
    >>> dijkstra(Si1,Sf,sif)
    (['E', 'B', 'C', 'S'], ['11','16','13'])
    """
    sommPoss=[] # On garde en mémoire la liste des chemins possibles pour chaque sommet
    P=[]
    predecesseur = [] # liste des sommets choisi et de leur predecesseur qui va permettre de retrouver le bon chemin
    vol1=[] # Pour savoir à quel vol correspond chaque tronçon
    long = 0 # Longueur du chemin parcouru
    mini = 0
    Si = Si1 # Car problème pour reconstituer chemin
    while Si != Sf:
        for i in range (0,len(sif)):
            present,p = fonc(sommPoss,sif[i][1])
 # variable qui indique si sif[i][1] est parmi les sommets qui ont deja pu etre parcourus
            if sif[i][0] == Si and present == False : # Le sommet n'a pas encore eu la possibilité d'être parcouru
                sommPoss.append((sif[i][1],float(sif[i][2])+long))
                predecesseur.append((sif[i][1],Si)) # On ajoute le sommet qu'on a choisi et son predecesseur
                vol1.append(sif[i][3])
            elif sif[i][0] == Si and present == True :
                if sommPoss[p][1] > float(sif[i][2])+long:
                    sommPoss=np.delete(sommPoss,p,0)
                    print(sommPoss)
                    sommPoss.append((sif[i][1],sif[i][2])) 
                    predecesseur.append((sif[i][1],Si))
                    vol1.append(sif[i][3])
        for j in range (0,len(sommPoss)):
            P.append(sommPoss[j][1]) # On recupere uniquement les poids possibles
        mini = min(P)
        pos = P.index(mini) # On recupere la position du minimum dans la matrice de poids et donc dans sommPoss
        long = mini # On ajoute le poids de l'arc choisi à la longueur du chemin 
        t=0
        while t <len(sif): # On ne peut pas parcourir un sommet plusieurs fois (dans un sens ou dans l'autre)
            if sif[t][0] == Si or sif[t][1] == Si: 
                sif2=np.delete(sif,t,0)
                sif = sif2
            else:
                t+=1    
        Si = sommPoss[pos][0] # On recupere le sommet suivant
        sommPoss.remove(sommPoss[pos]) # On enleve ce sommet de la liste des sommets possible => on ne peut plus le parcourir
        P = []
        sif = sif2
        present,p = fonc(predecesseur, Sf) # On commence par chercher le sommet final dans la liste predecesseur
        prede = predecesseur[p][1] # On recupere le prede de Sf
        vol2=[vol1[p]]
        chemin=[Sf,prede] # Chemin parcouru. La liste est remplie à l'envers. Il ne faut pas oublier d'ajouter le sommet final dans la liste
        while prede != Si1: # Tant qu'on a pas reconstitué le chemin jusqu'au sommet initial
            present,p = fonc(predecesseur,prede)
            prede = predecesseur[p][1]
            chemin.append(prede)
            vol2.append(vol1[p])
        chemin.reverse() # On remet la liste dans le bon sens
        vol2.reverse()
    return(chemin,vol2)

                
