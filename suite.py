from math import *
from cmath import sqrt
from fractions import Fraction
import matplotlib.pyplot as plt
from numpy import *

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

def fibo_2(n):
    n1 = 0
    n2 = 1
    for i in range(2, n+1):
        nextValue = n1 + n2 
        n1 = n2
        n2 = nextValue
        # TODO