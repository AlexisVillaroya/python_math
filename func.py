import datetime

def f1(x):
    return x**3-3*x+1

def balayage(f, a, pas):
    x = 0 
    while(f(x)*f(a)>0):
        x=x+pas
    return x

def dichotomie(f,a,b,precision):
    gauche = a
    droite = b
    while droite-gauche>precision:
        new_point=(gauche+droite)/2
        if f(new_point)*f(gauche)>0:
            gauche = new_point
        else:
            droite = new_point
    return new_point

def convertMsToDate(msec):
    return datetime.datetime.fromtimestamp(msec)