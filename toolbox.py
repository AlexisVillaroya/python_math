from cmath import sqrt
from fractions import Fraction

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
    