from numpy import *
import numpy

def addKey(pKey, pKeys):
    return pKeys.append(pKey)

def delKey(pKey, pKeys):
    return pKeys.remove(pKey)

def addVertex(pGraph, pKey, pKeys):
    """ Ajoute un sommet à la liste de sommet (pKeys)

    Args:
        pGraph (dict): graphe où l'on ajoute le sommet
        pKey (_type_): nom de la clé 
        pKeys (list): liste des sommets

    Returns:
        dict: graphe modifié
    """
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pKey not in pKeys):
            pGraph[pKey] = []
            addKey(pKey, pKeys)
    return pGraph

def addPath(pGraph, pPath1, pPath2, pKeys):
    """ Ajoute dans la liste d'adjacence du sommet pPath1
        le sommet pPath2

    Args:
        pGraph (dict): graphe où l'on ajoute le chemin
        pPath1 (_type_): sommet où l'on ajoute le sommet adjacent
        pPath2 (_type_): sommet à ajouter
        pKeys (list): liste des sommets

    Returns:
        dict: graphe modifié
    """
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pPath1 in pKeys):
            if(pPath2 not in pGraph[pPath1]):
                pGraph[pPath1].append(pPath2)
    return pGraph

def deleteVertex(pGraph, pKey, pKeys):
    """ Supprime un sommet à la liste de sommet (pKeys)

    Args:
        pGraph (dict): graphe où l'on supprime le sommet
        pKey (_type_): nom de la clé à supprimer
        pKeys (list): liste des sommmets

    Returns:
        dict: graphe modifié
    """
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pKey in pKeys):
            del pGraph[pKey]
            delKey(pKey, pKeys)
            for key in pKeys:
                deletePath(pGraph, key, pKey, pKeys)
    return pGraph

def deletePath(pGraph, pPath1, pPath2, pKeys):
    """ Supprime un chemin du graphe

    Args:
        pGraph (dict): graphe où l'on supprime le chemin
        pPath1 (_type_): sommet 1 où l'on supprime le chemin
        pPath2 (_type_): sommet 2 où l'on supprime le chemin
        pKeys (list): liste des sommets

    Returns:
        dict: graphe modifié
    """
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pPath2 in pGraph[pPath1]):
            pGraph[pPath1].remove(pPath2)
            if(pPath1 in pGraph[pPath2]):
                pGraph[pPath2].remove(pPath1)
    return pGraph

def generateMatrix(pGraph):
    size = len(pGraph)
    valRen = numpy.zeros((size, size))
    if(isinstance(pGraph, dict)):
        for key, listPath in pGraph.items():
            for val in listPath:
                valRen[key][val] = 1
    return valRen 

def existPath(pMat, pPath1, pPath2):
    n = len(pMat)
    

def degre(pGraph):
    """ Détermine le degre du graphe

    Args:
        pGraph (dict): graphe où l'on va chercher le plus haut degre

    Returns:
        int: degre
    """
    valRen = 0
    if(isinstance(pGraph, dict)):
        for key, listPath in pGraph.items():
            for val in listPath:
                if(val>valRen):
                    valRen = val
    return valRen

def listAccessVertex(pGraph, pKey):
    """ Liste des sommets accessible depuis un autre sommet (pKey)

    Args:
        pGraph (dicy): graphe à traiter
        pKey (_type_): sommet à traiter

    Returns:
        list: liste des sommets accessibles
    """
    valRen = []
    if(isinstance(pGraph, dict)):
        valRen = pGraph[pKey]
    return valRen

#def isConnected(pGraph):