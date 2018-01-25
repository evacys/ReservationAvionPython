import datetime
import numpy as np

date = datetime.datetime(2009, 6, 8, 23, 0)
fuseauHor = '+04:30'


def localToGreen(date,fuseauHor): 
    """ 
    Fonction qui permet de convertir une heure donnée en locale en une heure en Greenwitch
    
    param:
    
    date = date en local que l'on souhaite convertir en Greenwitch
    date de type : 2009-06-08 23:00:00
    fuseauHor = décalage de la ville par rapport au fuseau de Greenwitch
    fuseauHor : chaine de caractère '+ ou - heure:minute'
    """
    heure=[]
    minute=[]
    signe = fuseauHor[0]
    fuseauHor = fuseauHor.strip(signe) # On enlève le signe de la chaine pour pouvoir travailler sur l'heure uniquement
    F = str.split(fuseauHor,':')
    heure = F[0]
    if heure [0] == 0: # Si le premier nombre des heures est nul
        heure = int(heure[1])
    else:
        heure = int(heure[0]+heure[1])
    minute = F[1]
    if minute [0] == 0:
        minute = int(minute[1])
    else:
        minute = int(minute[0]+minute[1])
    if signe =='+':
        nouvDate = date - datetime.timedelta(hours=heure,minutes=minute) # On est en heure locale donc il y a des heures en plus p/r à Green, il faut donc retrancher le décalage 
    else:
        nouvDate = date + datetime.timedelta(hours=heure,minutes=minute)
    return nouvDate
            
def greenToLocal(date, fuseauHor):
    """ 
    Fonction qui permet de convertir une heure donnée en Greenwitch en une heure en local
    
    param:
    
    date = date en Greenwitch que l'on souhaite convertir en local
    date de type : 2009-06-08 23:00:00
    fuseauHor = décalage de la ville par rapport au fuseau de Greenwitch
    fuseauHor : chaine de caractère '+ ou - heure:minute'
    """
    heure=[]
    minute=[]
    signe = fuseauHor[0]
    fuseauHor = fuseauHor.strip(signe) # On enlève le signe de la chaine pour pouvoir travailler sur l'heure uniquement
    F = str.split(fuseauHor,':')
    heure = F[0]
    if heure [0] == 0: # Si le premier nombre des heures est nul
        heure = int(heure[1])
    else:
        heure = int(heure[0]+heure[1])
    minute = F[1]
    if minute [0] == 0:
        minute = int(minute[1])
    else:
        minute = int(minute[0]+minute[1])
    if signe =='+':
        nouvDate = date + datetime.timedelta(hours=heure,minutes=minute) # On est en heure Grenwitch donc il y a des heures en plus p/r à Green, il faut donc ajouter le décalage 
    else:
        nouvDate = date - datetime.timedelta(hours=heure,minutes=minute)
    return nouvDate
    