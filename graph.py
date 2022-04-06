# ajouterSommet
# ajouterChemin
# supSommet
# supChemin
# genererGraph

def ajouterSommet(dict, nom):
    size = len(dict)
    if(size == 0):
        dict[nom] = []
    else:
        dict[nom] = [0] * len(dict)

def ajouterChemin(dict, sommet, sommetVoisin):
    dict[sommet][sommetVoisin] = 1

def supSommet(dict, nom):
    del dict[nom]

def supChemin(dict, sommet, sommetVoisin):
    dict[sommet][sommetVoisin] = 0

def generateMatAdj(mat):
    sizeMat = len(mat)
    dict = {}
    for i in range(len(mat)):
        dict[i] = [0] * len(mat)
    for i in range(sizeMat):
        ajouterSommet(dict, i)
        for j in range(len(mat[i])):
            dict[i][j] = 1
    return dict 

def genererGraph():
    print('x')

# Exercice 1

def degre(dict):
    num = 0
    size = len(dict)
    for i in range(size):
        if(sum(dict[i]) > num):
            num = sum(dict[i])
    return num

# Exercice 2

def sommetAccess(dict, sommet):
    liste = []
    dict[sommet]