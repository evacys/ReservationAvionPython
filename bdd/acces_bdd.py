# -*- coding: utf-8 -*-

import sqlite3




def ouvrir_connexion(nom):
    """
    Connexion à une base de données SQLite

    :param nom: nom de la base de données
    :return: la base et un curseur sur la base
    """
    base = sqlite3.connect(nom)
    curseur = base.cursor()
    return(base,curseur)


def executer_requete(curseur, requete, variables = ()):
    """
    Exécution d'une requête SQL

    :param curseur: curseur sur la base de données
    :type curseur: sqlite3.Cursor
    :param requete: requête à exécuter
    :type requete: string
    :param variables: variables à insérer dans la requête
    :type variables: tuple
    :return: résultat de la requête
    :rtype: sqlite3.Cursor
    """
    resultat = None
    try:
        resultat = curseur.execute(requete,variables)
    except sqlite3.IntegrityError:
        print("integrity error")
        print(requete)
    except sqlite3.OperationalError:
        print("operational error")
        print(requete)
    except sqlite3.DataError:
        print("data error")
        print(requete)
    finally:
        return resultat     
    
    
def fermer_db(base, curseur):
    """
    Déconnexion de la base de données

    :param base: base SQLite
    :param curseur: curseur sur la base
    """
    curseur.close()
    base.close()
    


def valider_modif(base):
    """
    Validation des modifications d'une bdd

    :param base: bdd à mettre à jour
    """
    base.commit()


def annuler_modif(base):
    """
    Annulation des modifications d'une bdd

    :param base: bdd où annuler les modifications
    """
    base.rollback()
