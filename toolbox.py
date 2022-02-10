from cmath import sqrt
import math
from fractions import Fraction

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

def ineq(a, b):

    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []
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
    
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        symb ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []

    x = int(float(eq1(a, b)[1]))
    if symb == '>':
        result = ineq(a,b)
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

def calculerDelta(a,b,c):
    return b*b-4*a*c

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
        if(delta > 0):
            x1 = ((-b) - sqrt(delta)) / (2*a)
            x2 = ((-b) - sqrt(delta)) / (2*a)
            result = ['{',str(x1),';',str(x2),'}']
        elif(delta < 0):
            result = ["Pas de solution réel"]
        else:
            x = -b/(2*a)
            result = ['{',str(x),'}']
    else:
        result = ['Le discriminant n\'est pas un entier']
    return result

def ineq2(a,b,c):
    result = []

    delta = calculerDelta(a,b,c)
    if(isinstance(delta, int)):
        if(delta > 0):
            x1 = ((-b) - sqrt(delta)) / (2*a)
            x2 = ((-b) - sqrt(delta)) / (2*a)
            if a > 0:
                result = ['R - [',str(x1),';',str(x2),']']
            else:
                result = ['']

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

    