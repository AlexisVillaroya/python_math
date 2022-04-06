#from toolbox import *
from func import *
from training import *
import time
from graph import *

# test palindrome

# print(isPalindromeIter("bonjour"))
# print(isPalindromeIter("otto"))

# print(isPalindromeRec("bonjour"))
# print(isPalindromeRec("otto"))

# print(isPalindrome("bonjour"))
# print(isPalindrome("otto"))

# array = ["ab", "cb", "ab", "ab", "ft", "yu"]
# print(countOccur(array, "ab"))

#drawSuite(genSuite(suite1, 1, 100, 1))

# mat1 = [[1,2,3], [4,5,6]]
# mat2 = [[1,2,3], [4,5,6]]

# mat3 = [[1,1,1,1], [0,1,1,1], [0,0,1,1], [0,0,0,1]]
# mat4 = [[1,0,0,0], [1,1,0,0], [1,1,1,0], [1,1,1,1]]
# mat5 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

# print(is_triang_sup(mat3))
# print(is_triang_inf(mat4))
# print(is_diag(mat5))
# print(trace(mat5))
# display_matrice(copy_mat(mat1))

# mat = [[1,-1,2],[2,2,-2],[-1,1,2]]

# print(is_pseudomagique(mat))
# print(second_deg(0, 12, 3))
# print(somme_diag(mat, 0))


# print(suite1(10))
# print(suite_iter(4))
# print(suite_iter(4))
# print(depassement(341))
# draw_rep(20)

### TEST Fonctions

# tps1 = time.time()
# print("10 chiffres significatifs : ", balayage(f1,10,0.0001))
# tps2 = time.time()
# intervalletemps = tps2 - tps1

# print("Deuxième solution : ",balayage(f1,-0.5,0.0001))
# print("Troisième solution : ",balayage(f1,1,0.0001))

# print("Première solution : ", dichotomie(f1,-2,-1,0.0001))
# print("Deuxième solution : ",dichotomie(f1,-1,1,0.0001))
# print("Troisième solution : ",dichotomie(f1,1,2,0.0001))

### TEST Graphes

graphe1 = {0 : [0, 1, 0, 1], 1 : [0, 0, 1, 1], 2 : [1, 0, 1, 1], 3 : [1, 1, 1, 0]}
graphe2 = {}

mat = [[1,2],[3],[1,3],[0]]

# # Ajouter un sommet 
# print(ajouterSommet(graphe1, 4))
# # Ajouter un chemin
# print(ajouterChemin(graphe1, 4, 2))
# # degre
# print(degre(graphe1))

print(generateMatAdj(mat))
