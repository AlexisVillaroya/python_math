# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:00:02 2022

@author: Olivier TORREQUADRA
classe Matrice
MAJ 19/03/2022
"""

class Matrices():
    def __init__(self,pTaille=0,pType='Zero'):
        print("matrice créée")
        self.__mat=[]
        self.__inverse=[]
        self.__matW=[]
        self.__taille=pTaille
        if pType=='Zero':
            self.setZero(pTaille)

    def setZero(self,pTaille):
        #Créer une matrice carrée avec des 0
        valRen=False
        for i in range(pTaille):
            self.__mat.append([])
            for j in range(pTaille):
                self.__mat[i].append(0)
        return True

        
    def setTaille(self,pTaille=0):
        if self.__mat==[]:
            self.__taille=pTaille
        else:
            self.__taille=len(self.__mat)
    
    def setMat(self,pMat=[]):
        self.__mat=self.__copierMat(pMat)
        self.setTaille()

    def dupliquer(self):
        valRen=Matrices(self.__taille)
        for i,ligne in enumerate(self.__mat):
            for j,val in enumerate(self.__taille):
                valRen.setVal(i,j,val)
        return valRen

        
    def __copierMat(self,pSrc):
        valRen=[]
        for val in pSrc:
            valRen.append(val)
        return valRen
        
    def setID(self,pDest="M"):
        """
        créée une matrice identité dans la propriété passée en paramètre
        pDest : M=Matrice, I=inverse, W=travail
        """
        valRen=[]
        for i in range(self.__taille):
            valRen.append([])
            for j in range(self.__taille):
                val=0
                if i==j:
                    val=1
                valRen[-1].append(val)
                
        if pDest=="M":
            self.setMat(valRen)
        elif pDest=="I":
            self.__inverse=self.__copierMat(valRen)
        else:
            self.__matW=self.__copierMat(valRen)

    def setVal(self,pL,pC,pVal):
        print("Ajout val : ",pL,pC,pVal)
        self.__mat[pL][pC]=pVal

    def getVal(self,pL,pC):
        return(self.__mat[pL][pC])

    def getTaille(self):
        return(self)
    
    def afficher(self,pQuelleMat="M"):
        print("Affichage de la matrice ",pQuelleMat," de taille ",self.__taille)
        if pQuelleMat=="M":
           mat=self.__mat
        elif pQuelleMat=="I":
            mat=self.__inverse
        else:
            mat=self.__matW
        for ligne in mat:
            print(ligne)
        print("")
            
    def inverser(self):
        self.setID("I")

    def multiplierMatrice(self,pMat):
        valRen=Matrices(self.__taille)
        for i in range(len(valRen)):
            for j in range(len(valRen)):
                res=0
                for k in range(len(valRen)):
                    res+=self.getVal(i,k)*pMat.getVal(k,j)
                valRen.setVal(i,j,res)
        return valRen

    def rangN(self,pN):
        valRen=self.dupliquer()
        if pN>1:
            for i in range(pN-1):
                valRen=self.multiplierMatrice(valRen, self)
        return valRen

print("Import classe Matrice...success !")       
"""
mat1=Matrices()
mat1.setTaille(15)
mat1.setID()
mat1.afficher()
mat1.inverser()
mat1.afficher("I")
"""      

