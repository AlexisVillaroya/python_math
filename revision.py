import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4 - math.exp(-x) - x**2

# derivee de f
def df(x):
    return -math.exp(-x) - 2*x

def tracerCourbe(pF,pA,pB,pDt):
    lX=[]
    lY=[]
    for x in np.arange(pA,pB,pDt):
        lX.append(x)
        lY.append(pF(x))
    print(lX)
    print(lY)
    plt.plot(lX,lY)
    plt.show()

def balayage(pF,pA,pPas):
    pX = pA
    while(pF(pX) * pF(pA) > 0):
        pX += pPas
    return pX    

def dichotomie(pF,pA,pB,pPrec):
    pX = (pA + pB) / 2
    while(abs(pB - pA) > pPrec):
        if(pF(pX) * pF(pA) > 0):
            pA = pX
        else:
            pB = pX
        pX = (pA + pB) / 2
    return pX
    