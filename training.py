from math import *
from cmath import sqrt
from fractions import Fraction
import matplotlib.pyplot as plt
from numpy import *

from matrix import somme_line

def calculerDelta(a,b,c):
    return b*b-4*a*c

def eq1(a, b):
    result = []

    if(isinstance(a, int) and isinstance(b, int)):
        if a==0:
            if b==0:
                result = [']','-∞',';','+∞','[']
            else:
                result = ['Ensemble vide']
        else:
            if b==0:
                result = [1/a]
            else:    
                result = [-b/a]
    return result

# Exercice 1

# .1

def second_deg(a, b, c):
    result = []

    delta = calculerDelta(a,b,c)
    if(isinstance(delta, int)):
        # N'admet qu'une solution 
        if a==0:
            result = eq1(b,c)
        else:
            if(delta > 0):
                x1 = ((-b) - sqrt(delta)) / (2*a)
                x2 = ((-b) - sqrt(delta)) / (2*a)
                result = [x1,x2]
            elif(delta < 0):
                result = None
            else:
                x = -b/(2*a)
                result = [x]
    else:
        result = None
    return result

# .2

def changvar2(a, b, c):
    ret = second_deg(a, b, c)
    ret2 = []
    if ret != 0:
        for val in ret:
            ret2.append(1/val)
    else:
        ret2.append(0)
    return ret2


# Exercice 2

# .1

def somme_lig(mat, ligne):
    if(isinstance(mat, list)):
        return sum(mat[ligne])
    else:
        raise ValueError("It's not a list")

# .2

def somme_row(mat, row):
    if(isinstance(mat, list)):
        total = 0
        for line in mat:
            total += line[row]
        return total
    else:
        raise ValueError("It's not a list")

# .3

def is_pseudomagique(mat):
    ret = True
    if(isinstance(mat, list)):
        for i in range(len(mat)):
            if(somme_lig(mat, i) != 2 and somme_row(mat, i) != 2):
                ret = False
    return ret    

# .4

def somme_diag(mat, nBool):
    ret = 0
    n = len(mat)
    if(nBool == 1):
        ret = sum(mat[i][i] for i in range(n))
    elif(nBool == 0):
        ret = sum(mat[i][n-i-1] for i in range(n))
    else:
        ret = None
    return ret


def is_magique(mat):
    ret = False
    if(isinstance(mat, list) and is_pseudomagique(mat)):
        if(somme_diag(mat, 0) == 2 and somme_diag(mat, 1) == 2):
            ret = True
    return ret


