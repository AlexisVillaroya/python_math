from math import *
from cmath import sqrt

def copy_mat(mat):
    if(isinstance(mat, list)):
        ret = []
        for line in mat:
            ret.append(line[:])
    else:
        raise ValueError("It's not a list")
    return ret

def display_matrice(mat):
    if(isinstance(mat, list)):
        for line in mat:
            print(line)
    else:
        raise ValueError("It's not a list")

def somme_line(mat, ligne):
    if(isinstance(mat, list)):
        return sum(mat[ligne])
    else:
        raise ValueError("It's not a list")

def somme_row(mat, row):
    if(isinstance(mat, list)):
        total = 0
        for line in mat:
            total += line[row]
        return total
    else:
        raise ValueError("It's not a list")

def permut_line(mat, p1, p2):
    if(isinstance(mat, list)):
        ret = copy_mat(mat)
        tmp = ret[p1][:]
        ret[p1] = ret[p2][:]
        ret[p2] = tmp[:]
    else:
        raise ValueError("It's not a list")
    return ret


# Exercice 1

def is_triang_sup(mat):
    ret = True
    for i in range(1, len(mat)):
        for j in range(0, i):
            if(mat[i][j] != 0):
                ret = False
    return ret

def is_triang_inf(mat):
    n=len(mat)
    ret = True
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(mat[i][j] != 0):
                ret = False
    return ret

def is_diag(mat):
    return is_triang_sup(mat) == is_triang_inf(mat)

# Exercice 2

def trace_mat(mat):
    Sum = 0 
    if(is_diag(mat) != True):
        raise ValueError("It's not a diagonal matrix")
    else:
        for i in range(len(mat)):
            for j in range(len(mat)):
                Sum += mat[i][j]
    return Sum

# Exercice 3

def somme_mat(mat1, mat2):
    ret = []
    if(len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        raise ValueError("The matrix are not the same size")
    else:
        ret = copy_mat(mat1)
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                ret[i][j] = mat1[i][j] + mat2[i][j]
    return ret

def prod_mat(mat1, mat2):
    ret = []
    # Fill the matrice with null value
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            row.append(0)
        ret.append(row)

    # Multiply matrices
    if(len(mat1[0]) != len(mat2)):
        raise ValueError("Line and row are not the same size")
    else:
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    ret[i][j] = mat1[i][k] * mat2[k][j]
    return ret


def puiss_mat(A, k):
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            A[i][j] = k * A[i][j]
    return A