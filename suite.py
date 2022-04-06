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

# Exercice 5

def suite5_iter(n):
    u=2
    v=-1
    for i in range(1,n+1):
        temp=u-2*v
        v=u+3*v
        u=temp
    return u,v

def suite5_rec(n):
    if n==0:
        return [2,-1]
    else:
        u=suite5_rec(n-1)[0]-2*suite5_rec(n-1)[1]
        v=suite5_rec(n-1)[0]+3*suite5_rec(n-1)[1]
    return [u,v]

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
    liste=[1,1]
    for i in range(2,n+1):
        val=liste[-1]+liste[-2]
        liste.append(val)
    return liste

def fibo_2(n):
    u=1
    v=1
    for i in range(2,n+1):
        w=u+v
        u=v
        v=w
    return v

def fibo_3(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo_3(n-1)+fibo_3(n-2)
    
def conv_fibo():
    u=1
    v=1
    n=0
    phi=(1+sqrt(5))/2
    while abs(v/u-phi)>10**(-4):
        n=n+1
        w=u+v
        u=v
        v=w
    return n

# Suite de Syracuse

# Question 1
    
def syracuse(a,n):
    u=a
    print(a)
    for i in range(1,n+1):
        if u%2==0:
            u=u/2
        else :
            u=3*u+1
        print(u)

# Questions suivantes
     
def traj(n):
    u=n
    c=0
    maxi=n
    while u!=1:
        c=c+1
        if u%2==0:
            u=u/2
        else:
            u=3*u+1
        if maxi<u:
            maxi=u
        print(u)
    print('la durée de vol est : ',c,' et l''altitude est : ',maxi)
    

# Suite de Sylvester

def sylvester_iter(n):
    s=2
    prod=2
    for i in range(1,n+1):
        s=1+prod
        prod=prod*s
    return s

def sylvester_rec(n):
    if n==0:
        return 2
    else:
        prod=1
        for i in range(n):
            prod=prod*sylvester_rec(i)
        return 1+prod     # cette fonction n'est vraiment pas intéressante au niveau de l'optimisation
    
def sylvester2_iter(n):
    s=2
    for i in range(1,n+1):
        s=1+s*(s-1)
    return s

def sylvester2_rec(n):
    if n==0:
        return 2
    else:
        return 1+sylvester2_rec(n-1)*(sylvester2_rec(n-1)-1)
    
def nb_chiffres(n):
    s=2
    for i in range(1,n+1):
        s=1+s*(s-1)
    return len(str(s))

def trace_syl(n):
    x=range(0,n+1)
    y=[nb_chiffres(i) for i in x]
    plt.plot(x,y)
    
def conv_syl(a):
    somme=0
    n=0
    while 1-somme>=a:
        somme+=1/sylvester2_iter(n)
        n=n+1
    return n-1
    