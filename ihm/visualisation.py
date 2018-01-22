import sys
#sys.path.append(r'C:\Users\Eva\Documents\Cours_ENSG\Projet_info\projet\projet')
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\Mes documents\School\ING1\Informatique\Projet Informatique\Projet')

from fonction.tracer_carte import *
from ihm.trajet import verif_date,convert_date


def visualisation(vols):
    dateDeb = input('Date de début de visualisation (YYYY-MM-DD hh:mm): ')
    valide1 = verif_date(dateDeb)
    while valide1 == False:
        print('La date rentrée est non valide')
        dateDeb = input('Date de début de visualisation (YYYY-MM-DD hh:mm): ')
        valide1 = verif_date(dateDeb)
    
    dateFin = input('Date de fin de visualisation (YYYY-MM-DD hh:mm): ')    
    valide2 = verif_date(dateFin)
    while valide2 == False:
        print('La date rentrée est non valide')
        dateFin = input('Date de fin de visualisation (YYYY-MM-DD hh:mm): ')
        valide2 = verif_date(dateFin)
        
    dateDeb = convert_date(dateDeb)
    dateFin = convert_date(dateFin)
    print('Les vols prévus sont les suivants:')
    mercator_plus_tous_les_vols(vols,dateDeb,dateFin)
    return ('------')