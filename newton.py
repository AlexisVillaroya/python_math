import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**3-3*x+1

def f2(x):
    return 3*x**3-2*x**2+x+2
    
def df2(x):
    return 9*x**2-4*x+1

# Tracé de f1
x=np.linspace(1,2,30)
y=f1(x)
plt.plot(x,y)


def dicho(f,a,b,prec):
    while b-a>prec:
        c=(a+b)/2
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    return c


def secantes(f,a,b,prec):
    while b-a>prec:
        c=a-(b-a)/(f(b)-f(a))*f(a)
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    return c

# Tests
print(dicho(f1,1,2,0.001))
print(secantes(f1,1,2,0.001))

def newton(f,df,x0,prec):
    u=x0
    if df(u)!=0:
        v=u-f(u)/df(u)
    else:
        return None
    while abs(v-u)>prec:
        if df(v)!=0:
            u=v
            v=v-f(v)/df(v)
        else:
            return None
    return v