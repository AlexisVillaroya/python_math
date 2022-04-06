"""
Classe Graphes
Olivier TORREQUADRA
MAJ 06/04/2022
"""
import classeMatrice2022 as m
class Graphes():
    def __init__(self,pGraphe={}):
        if isinstance(pGraphe,dict)==True:
            self.__dico=pGraphe.copy()
    def __str__(self):
        """
        retourner le nom des sommets dans une chaine de caractères
        """
        valRen=""
        for sommet in self.__dico.keys():
            valRen+=str(sommet)+"-"
        return valRen
    def ajouterSommet(self,pS):
        valRen=False
        if pS not in self.__dico.keys():
            self.__dico[pS]=[]
            valRen=True
        return valRen
    def ajouterSommets(self,pSommets=[]):
        """
        Ajouter les sommets de la liste dans le graphe
        """
        valRen=False
        if isinstance(pSommets,list):
            for s in pSommets:
                self.ajouterSommet(s)
            valRen=True
        return valRen
    def ajouterChemin(self, pS1,pS2):
        valRen=False
        if pS1 in self.__dico.keys():
            if pS2 not in self.__dico[pS1]:
                self.__dico[pS1].append(pS2)
                valRen=True
        return valRen

    def genererMatrice(self):
        print("Génération matrice")
        valRen=m.Matrices(len(self.__dico))
        valRen.afficher()
        for noeud, lstChemins in self.__dico.items():
            for val in lstChemins:
                valRen.setVal(noeud,val,1)            
        return valRen

    def existeCheminL(self,pS1,pS2,pL):
        valRen=False
        matN=self.genererMatrice().rangN(pL)
        if matN.getVal(pS1,pS2)>0:
            valRen=True
        return valRen

    def existeChemin(self,pS1,pS2):
        valRen=-1
        lgCh=1
        repTrouvee=False #la réponse a t elle été trouvée
        matA=self.genererMatrice()
        while repTrouvee==False:
            if lgCh>matA.getTaille():
                repTrouvee=True
            else:
                repTrouvee=self.existeCheminL(pS1,pS2,lgCh)
                if repTrouvee==False:
                    lgCh+=1
                else:
                    valRen=lgCh
        return valRen
    def fQuelChemin(self,pS1,pS2):
        valRen=[]
        matA=self.genererMatrice()
        lgCh=self.existeChemin(pS1,pS2)
        if lgCh>0:
            valRen.append(pS1)
            while len(valRen)<lgCh:
                lSuccesseur=self.__dico[valRen[-1]]
                i=0
                while self.existeCheminL(lSuccesseur[i],pS2,lgCh-len(valRen))==False:
                    print(lSuccesseur[i],pS2,lgCh-len(valRen))
                    i+=1
                valRen.append(lSuccesseur[i])
            valRen.append(pS2)       
        return valRen


g1=Graphes()
print(g1)
g1.ajouterSommet(0)
print(g1)
g1.ajouterSommets([1,2,3,4])
print(g1)

g1.ajouterChemin(0,4)
g1.ajouterChemin(1,0)
g1.ajouterChemin(1,2)
g1.ajouterChemin(1,3)
g1.ajouterChemin(2,4)
g1.ajouterChemin(2,0)
g1.ajouterChemin(3,2)
g1.ajouterChemin(4,1)
g1.ajouterChemin(4,3)

g1.genererMatrice()

m1=g1.genererMatrice()
m1.afficher()
# print(g1.existeChemin(0,1))

