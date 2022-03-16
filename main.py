from toolbox import *

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

mat1 = [[1,2,3], [4,5,6]]
mat2 = [[1,2,3,], [4,5,6]]

mat3 = [[1,1,1,1], [0,1,1,1], [0,0,1,1], [0,0,0,1]]
mat4 = [[1,0,0,0], [1,1,0,0], [1,1,1,0], [1,1,1,1]]
mat5 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

# print(is_triang_sup(mat3))
# print(is_triang_inf(mat4))
# print(is_diag(mat5))
# print(trace(mat5))
print(prod_mat(mat1, mat2))
