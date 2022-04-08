import random

# Exercice 1 

def randomSix():
    pTruque = random.randint(1, 4)
    valRen = 0
    if(pTruque == 1): # 1/4 de chance de renvoyer 0
        valRen = random.randint(0,1)
        if(pTruque == 1):
            valRen = 6
        else:
            valRen = random.randint(0,5)
    else:
        valRen = random.randint(1,6)
        
    return valRen

# Exercice 2

def simuleLancer():
    liste = []
    for i in range(10):
        liste.append(randomSix())
    return liste

def afficheMaxAndMin(liste):
    print("Max: ", max(liste))
    print("Min: ", min(liste))

# Exercice 3

def hasard():
    alea = random.randint(0,1)
    if(alea == 0):
        return -1
    else:
        return 1

def puce(n):
    pointAbscise = 0
    for t in range(0, n):
        t = t + 1
        pointAbscise = pointAbscise + hasard()
    return pointAbscise

# Exercice 4

def plusOuMoins():
    n = random.randint(1,100)
    print("Devinez le nombre entre 1 et 100")
    while(True):
        try:
            nb = int(input("Votre nombre: "))
            if(nb == n):
                print("Bravo, vous avez trouvé le nombre mystère")
                break
            elif(nb > n):
                print("Trop Grand")
            elif(nb < n):
                print("Trop petit")
        except:
            print("Vous n'avez pas saisi un nombre")

# Exercice 5

def binomial(n,p):
    nb_sucess = 0
    for i in range(0,n):
        if(random.random() < p):
            nb_sucess = nb_sucess + 1
    return nb_sucess

def moyenne(func, n, p):
    somme = 0
    for i in range(0,100):
        somme = somme + func(n, p)
    return somme/100

# Exercice 6

def simule100LancerDes():
    liste = []
    for i in range(100):
        liste.append(random.randint(1,6))
    return liste

def frequenceApparition(liste):
    seen = []
    for i in liste:
        if i not in seen:
            seen.append(i)
    freq = [0] * len(seen)
    for i in range(0, len(liste)):
        for j in range(0, len(seen)):
            if liste[i] == seen[j] and (j in liste):
                freq[seen.index(j)] = freq[seen.index(j)] + 1
    return freq

# Exercice 7



