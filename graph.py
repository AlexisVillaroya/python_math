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
                if(pPath1 not in pGraph[pPath2]):
                    pGraph[pPath2].append(pPath1)
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

def existPath(pGraph, pPath1, pPath2):
    """ Détermine si un chemin existe

    Args:
        pGraph (dict): graphe à traiter
        pPath1 (_type_): sommet 1
        pPath2 (_type_): sommet 2

    Returns:
        bool: True si le chemin existe, False sinon
    """
    valRen = False
    if(isinstance(pGraph, dict)):
        if(pPath1 in pGraph):
            if(pPath2 in pGraph[pPath1]):
                valRen = True
    return valRen
    
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

def listAccessVertex(pGraph, pKey, sizeGraph):
    """ Détermine la liste des sommets accessibles depuis un sommet

    Args:
        pGraph (dict): graphe à traiter
        pKey (_type_): sommet à traiter

    Returns:
        list: liste des sommets accessibles
    """
    valRen = []
    keys = [n for n in pGraph.keys()]
    if sizeGraph<0:
        return set(valRen)
    else:
        if(isinstance(pGraph, dict)):
            for i in pGraph.keys():
                # print('i', i)
                # print('pKey', pKey)
                # print(existPath(pGraph, i, pKey))
                # print('')
                if(pKey != i and existPath(pGraph, i, pKey)):
                    valRen.append(i)
                    val = i 
                else:
                    val = []
                valRen+=listAccessVertex(pGraph, val, sizeGraph-1)   
        return set(valRen)

def isConnected(pGraph):
    """ Détermine si le graphe est connexe

    Args:
        pGraph (dict): graphe à traiter

    Returns:
        bool: True si le graphe est connexe, False sinon
    """
    valRen = True
    if(isinstance(pGraph, dict)):
        for key in pGraph.keys():
            taille = len(listAccessVertex(pGraph, key, len(pGraph)))
            print('taille', taille)
            if taille < len(pGraph):
                valRen = False
    return valRen

def floyd(A):
    """ Algorithme de Floyd-Warshall

    Args:
        A (matrix): matrice du graphe

    Returns:
        matrix: matrice des distances
    """
    n = len(A)
    D = A.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

def access(liste,i):
    nb_etapes=[[i]]
    dejavu=[i]
    for k in range(1,len(liste)):
        new=[]
        for val in nb_etapes[k-1]:
            for j in liste[val]:
                if j not in dejavu:
                    dejavu.append(j)
                    new.append(j)
        nb_etapes.append(new)
    return [nb_etapes,dejavu]


def is_connexe(liste):
    valRen=True
    for i in range(len(liste)):
        nb_points_acc=len(access(liste,i)[1])
        if nb_points_acc<len(liste):
            valRen=False
    return valRen

def isTree(pGraph):
    """ Détermine si le graphe est un arbre

    Args:
        pGraph (dict): graphe à traiter

    Returns:
        bool: True si le graphe est un arbre, False sinon
    """
    valRen = False
    if(isinstance(pGraph, dict)):
        if(len(pGraph)>0):
            valRen = True
            for key, listPath in pGraph.items():
                for val in listPath:
                    if(val not in listAccessVertex(pGraph, key)):
                        valRen = False
    return valRen

