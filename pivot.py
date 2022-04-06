# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:17:47 2021

@author: Raphaël
"""

def permutation(M,i,j):
    # permute les lignes i et j de la matrice M
    temp=M[i][:]
    M[i]=M[j][:]
    M[j]=temp
    
def combinaison(M,a,i,b,j):
    #remplace Li par aLi+bLj
    for k in range(len(M)):
        M[i][k]=a*M[i][k]+b*M[j][k]

# Première étape : nettoyer sous la diagonale afin d'obtenir une matrice triangulaire supérieure 
def nettoyage(M,N,j):
    # détermine un pivot sur la colonne j puis nettoie M sous ce pivot et effectue les mêmes opérations sur N
    i=j
    piv=M[i][j]
    inv=True
    # on cherche ensuite un pivot non nul
    while piv==0 and i<len(M):
        i=i+1
        if i<len(M):
            piv=M[i][j]
    # on permute les deux lignes si besoin
    if i<len(M):
        if i!=j:
            permutation(M,i,j)
            permutation(N,i,j)
        for k in range(j+1,len(M)):
            coeff=M[k][j]
            combinaison(M,piv,k,-coeff,j)
            combinaison(N,piv,k,-coeff,j)
    else:
        inv=False
    return inv

def descente(M,N):
    # on effectue les opérations élémentaires jusqu'à obtenir une matrice triangulaire supérieure
    # on fait donc apparaitre des 0 sous les différents pivots
    continuer=True
    k=0
    while continuer and k<len(M):
        continuer=nettoyage(M,N,k) # on arrête l'algo dès qu'il est impossible de trouver un pivot non nul
        k=k+1
    return continuer


# Deuxième étape : nettoyer au-dessus de la diagonale pour obtenir une matrice diagonale
def montee(M,N):
    # On remonte la diagonale en faisant apparaitre des 0 au-dessus des différents pivots
    for j in range(len(M)-1,-1,-1):
        for i in range(j-1,-1,-1):
            coeff1=M[j][j]
            coeff2=M[i][j]
            combinaison(M,coeff1,i,-coeff2,j)
            combinaison(N,coeff1,i,-coeff2,j)


# Troisième étape : diviser chaque ligne par le bon coefficient pour obtenir la matrice identité
def lastop(M,N):
    # Une fois la matrice diagonale obtenue, on divise simplement les coefficients diagonaux par leurs valeurs
    for i in range(len(M)):
        coeff=M[i][i]
        for j in range(len(M)):
            M[i][j]=M[i][j]/coeff
            N[i][j]=N[i][j]/coeff
            

# Algorithme complet utilisant les procédures et fonctions précédentes         
def inverse(M):
    test=True
    # initialisation de la matrice identité
    I=[[0 for i in range(len(M))] for i in range(len(M))]
    for k in range(len(M)):
        I[k][k]=1
    print(I)
    # copie de M
    Mbis=[[M[i][j] for j in range(len(M))] for i in range(len(M))]
    print(Mbis)
    test=descente(Mbis,I)
    print(Mbis,I)
    if test:
        montee(Mbis,I)
        print(Mbis,I)
        lastop(Mbis,I)
        return I
    else:
        return []
    # on retourne une liste vide si la matrice n'est pas inversible