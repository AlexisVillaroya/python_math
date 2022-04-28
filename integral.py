# -*- coding: utf-8 -*-
"""

@author: Olivier TORREQUADRA
3ICS
Intégrale
"""
from cmath import sqrt
from code import interact
from curses.textpad import rectangle
import math as m
import matplotlib.pyplot as plt
import numpy as np
from random import random

def f(x):
    return m.exp(x)-x

def f2(x):
    return -3*x*x + 5*x +10


def fRectGauche(pF,pA,pB,pNb):
    
    valRen=0#aire totale
    dt=(pB-pA)/pNb
    x1=pA
    for i in range(pNb):
        x2=x1+dt
        valRen+=dt*pF(x1)
        x1=x2
    return valRen

def fTrapeze(pF,pA,pB,pNb):

    valRen=0#aire totale
    dt=(pB-pA)/pNb
    x1=pA
    for i in range(pNb):
        x2=x1+dt
        valRen+=dt*(pF(x1)+pF(x2))/2
        x1=x2
    return valRen

def tracerRectangle(pF,pA,pB,pNbR):
    lX=np.linspace(pA,pB,pNbR)
    print("LX:",lX)
    for i,x in enumerate(lX[:-1]):
        x2=lX[i+1]
        xRec=[x,x,x2,x2,x]
        yRec=[0,pF(x),pF(x),0,0]
        plt.plot(xRec,yRec,"r")
       
def tracerTrapeze(pF,pA,pB,pNbR):
    #Aire = (B+b)*h/2
    lX=np.linspace(pA,pB,pNbR)
    print("LX:",lX)
    for i,x in enumerate(lX[:-1]):
        x2=lX[i+1]
        xRec=[x,x,x2,x2,x]
        yRec=[0,pF(x),pF(x2),0,0]
        plt.plot(xRec,yRec,"g")  

def monteCarlo(pF,pA,pB,pNbR):
    aireRectangle= (maximum(pF, pA, pB, 1) * pB)
    compteur = 0
    for i in range(pNbR):
        x = random(pA, pB)
        y = random(0, maximum(pF, pA, pB, 1))
        if(pF(x)>=y):
            compteur += 1
    valRen = (compteur / pNbR) * aireRectangle # Aire approchée
    return valRen
       
# Calcul le maximum de f sur [a,b]
def maximum(f, a, b, pas):
    if(b<a):
        a, b = b, a
    x = a
    maximum = f(a)
    while(x<=b):
        y=f(x)
        if(y>maximum):
            maximum=y
        x+=pas
    return maximum

"""
tracerCourbe(f,0,1,0.01)
tracerRectangle(f,0,1,20)
tracerTrapeze(f,0,1,20)

for n in range(2,1000):
    print(n," rect : ",fRectGauche(f,0,1,n))
  
plt.show()

tracerCourbe(f2,-10,10,0.1)
plt.show()
print(1000," rect : ",fRectGauche(f,0,1,1000))
print(20," Trap : ",fTrapeze(f,0,1,20))
"""



        
        