
"""
Nous allons tester les méthodes de balayage et de dichotomie sur l'a résolution de l'équation
x^3+1=3x proposée dans le TP
"""
import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction dont on cherche une racine (point d'annulation)
def f1(x):
    return x**3-3*x+1


# Tracé de la fonction pour repérer un intervalle contenant la racine
x=np.linspace(-2,2,100)
y=f1(x)
plt.plot(x,y)
plt.show

# On s'aperçoit que la fonction f1 s'annule 3 fois sur [-2,2]

# cherche un changement de signe dans les images, en partant de l'abscisse a
def balayage(f,a,pas):
    x=a
    while f(x)*f(a)>0:
        x=x+pas
    return x

#Tests :
print("Première solution : ", balayage(f1,-2,0.0001))
print("Deuxième solution : ",balayage(f1,-0.5,0.0001))
print("Troisième solution : ",balayage(f1,1,0.0001))

# Raisonnons maintenant par dichotomie
def dichotomie(f,a,b,precision):
    gauche=a
    droite=b
    while droite-gauche>precision:
        new_point=(gauche+droite)/2
        print(f(new_point)*f(gauche)) 
        if f(new_point)*f(gauche)>0:
            gauche=new_point
        else:
            droite=new_point
    return new_point

#Tests :
print("Première solution : ", dichotomie(f1,-2,-1,0.0001))
print("Deuxième solution : ",dichotomie(f1,-1,1,0.0001))
print("Troisième solution : ",dichotomie(f1,1,2,0.0001))

