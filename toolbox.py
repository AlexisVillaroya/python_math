from math import *
from cmath import sqrt
from fractions import Fraction
import fractions
from re import X
import matplotlib.pyplot as plt
from numpy import array

def calculerDelta(a,b,c):
    return b*b-4*a*c

def displayEq(func):

    """ Affiche l'intervalle sous un format normalisé

    Args:
        func (function)
    """
    x = ''.join(func)
    print(x)


def eq1(a, b):

    """ Résoud l'équation ax + b = 0

    Args:
        a (float)
        b (float)

    Returns:
        [list]: Liste contenant le résultat de l'équation
    """
    result = []

    if(isinstance(a, int) and isinstance(b, int)):
        if a==0:
            if b==0:
                result = [']','-∞',';','+∞','[']
            else:
                result = ['Ensemble vide']
        else:
            if b==0:
                result = ['{', str(1/a), '}']
            else:    
                result = ['{', str(-b/a), '}']
    return result

def ineq1(a, b):

    """ Résoud l'inéquation ax + b > 0

    Args:
        a (float)
        b (float)

    Returns:
        [list]: Liste contenant le résultat de l'inéquation
    """
    result = []

    if a==0: 
        return eq1(a,b)
    else:
        x = int(float(eq1(a, b)[1]))


    if(isinstance(x, int)):
        if a > 0:
            result = [']',str(x),';','+∞','[']
        elif a < 0:
            result = [']','-∞',';',str(x),'[']
    else:
        result = ['Le résultat de l\'équation n\'est pas un entier']
    return result    

def ineq1bis(a,b,symb):
    
    """ Résoud les inéquations ax + b > 0 ou ax + b < 0
    Args:
        a (float): 
        b (float): 
        symb (string): 

    Returns:
        [list]: Liste contenant le résultat de l'inéquation
    """
    result = []

    x = int(float(eq1(a, b)[1]))
    if symb == '>':
        result = ineq1(a,b)
    elif symb == '<':
        if(isinstance(x, int)):
            if a > 0:
                result = [']','-∞',';',str(x),'[']
            elif a < 0:
                result = [']',str(x),';','+∞','[']
        else:
            result = ['Le résultat de l\'équation n\'est pas un entier']
    else:
        result = ['Mauvais symbole']
    return result

def ineq1bis2(a,b,symb):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        symb ([type]): [description]

    Returns:
        [type]: [description]
    """
    if symb == '>':
        return ineq1(a,b)
    elif symb == '<':
        return ineq1(-a,-b)

def eq2(a,b,c):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []

    delta = calculerDelta(a,b,c)
    if(isinstance(delta, int)):
        if a==0:
            result = eq1(b,c)
        else:
            if(delta > 0):
                x1 = ((-b) - sqrt(delta)) / (2*a)
                x2 = ((-b) - sqrt(delta)) / (2*a)
                result = ['{',str(x1),';',str(x2),'}']
            elif(delta < 0):
                result = ['Pas de solution réel']
            else:
                x = -b/(2*a)
                result = ['{',str(x),'}']
    else:
        result = ['Le discriminant n\'est pas un entier']
    return result

def ineq2(a,b,c):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []

    delta = calculerDelta(a,b,c)
    if(isinstance(delta, int)):
        if a==0:
            result = ineq1(b, c)
        else:
            if(delta > 0):
                if a > 0:
                    x1 = ((-b) - sqrt(delta)) / (2*a)
                    x2 = ((-b) + sqrt(delta)) / (2*a)
                    result = ['R - [',str(x1),';',str(x2),']']
                else:
                    x1 = ((-b) + sqrt(delta)) / (2*a)
                    x2 = ((-b) - sqrt(delta)) / (2*a)
                    result = ['R - [',str(x1),';',str(x2),']']
            elif(delta < 0):
                if a > 0:
                    result = ["Ensemble R"]
                else:
                    result = ["Pas de solution réel"]
            else:
                x = -b/(2*a)
                result = ['{',str(x),'}']
    else:
        result = ['Le discriminant n\'est pas un entier']
    return result

def ineq2bis(a,b,c,symb):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]
        symb ([type]): [description]

    Returns:
        [type]: [description]
    """
    if symb=='>':
        return ineq2(a,b,c)
    else:
        return ineq2(-a,-b,-c)



""" Si la chaine de caractère est un palindrome renvoi vrai

    Args:
        array ([type]): [description]

    Returns:
        [type]: [description]
"""

def isPalindromeIter(array):
    result = False
    if(isinstance(array, str)):
        for i in range(len(array)//2):
            if(array[i] == array[len(array)-i-1]):
                result = True
            else:
                result = False
    else:
        print("Error : wrong type")

    return result

def isPalindromeRec(array):
    result = False
    if(isinstance(array, str)):
        if(len(array) < 2):
            result = True
        else:
            if(array[0] == array[len(array)-1]):
                middleArray = array[1:len(array):-1]
                result = isPalindromeRec(middleArray)
            else:
                result = False
    else:
        print("Error : wrong type")
    return result 

def isPalindrome(array):
    return array == array[::-1]

def countOccur(array, n):
    """ Compte le nombre d'occurance dans une chaine 
    Args:
        array ([type]): [description]
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []
    if len(array) == 0:
        return 0
    result = (array[0] == n) + countOccur(array[1:], n)
    return result


# # # # # # # 
#           #
#   TP--1   #
#           #
# # # # # # #

# Exercice 1 

def suite1(pX):
    return log1p(1/pX)

def suite2(pX):
    return 3*exp(-1)**pX

def suite3(pX):
    return sqrt((pX**2)+1) - sqrt(pX)

def genSuite(pF, pDep, pArr, pPas):
    list_x = []
    list_y = []
    for i in range(pDep, pArr+pPas, pPas):
        list_x.append(i)
        list_y.append(pF(i))
    return list_x, list_y

def drawSuite(array):
    plt.plot(array[0], array[1])
    plt.show()

# Exercice 2

def ex2_iter(n):
    u=2
    for i in range(1, n+1):
        u=u/3+1
    return u 

def ex2_rec(n):
    if n==0:
        return 2
    else:
        return ex2_rec(n-1)/3+1
    
# Exerice 3

def ex3_iter(n):
    u=1
    for i in range(1, n+1):
        u=(u**2)//sqrt(exp(-u)+2)
    return u


def genSuite2(pF, listVal, nVal):
    while(len(listVal)<nVal):
        nextVal = pF(listVal)
        listVal.append(nextVal)
    return listVal

# Exercice 6

def termValue(n):
    Un = 0
    S = 0
    for k in range(n+1):
        Un = 1/(3**k)
        S += Un
    return Un

def trace(n):
    x = range(n+1)
    y = []
    s = 0
    for i in x:
        s = s+(1/3)**i
        y.append(s)
    plt.plot(x, y, "go")
    plt.show()
    
def minInt():
    s = 0
    k = 0
    while abs(s-1.5)>=10**(-6):
        k = k+1
        s += (1/3)**k
    return k

# Exercice 7

def termValue(n):
    Un = 0
    S = 0
    k = 1
    for k in range(n+1):
        Un = 1/(k*(1+k))
        S += Un
    return Un

def trace(n):
    x = range(1, n+1)
    y = []
    for i in x:
        s = s+1/(i*(1+i))
        y.append(s)
    plt.plot(x, y, "go")
    plt.show()
    
def minInt():
    s = 0
    k = 0
    while abs(s-1)>=10**(-6):
        k = k+1
        s += 1/(k*(1+k))
    return k

# Exercice 8

def fibo_1(n):
    n1 = 0
    n2 = 1
    list_fib = [n1,n2]
    for i in range(2, n+1):
        nextValue = n1 + n2
        list_fib.append(nextValue)
        n1 = n2
        n2 = nextValue 
    return list_fib 

    








