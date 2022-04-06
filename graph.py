def addKey(pKey, pKeys):
    return pKeys.append(pKey)

def addVertex(pGraph, pKey, pKeys):
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pKey not in pKeys):
            pGraph[pKey] = []
            addKey(pKey, pKeys)
    return pGraph

def addPath(pGraph, pPath1, pPath2, pKeys):
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pPath1 in pKeys):
            if(pPath2 not in pGraph[pPath1]):
                pGraph[pPath1].append(pPath2)
    return pGraph

def deleteVertex(pGraph, pKey, pKeys):
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if(pKey in pKeys):
            del pGraph[pKey]
    return pGraph

def deletePath(pGraph, pPath1, pPath2, pKeys):
    if(isinstance(pKeys, list) and isinstance(pGraph, dict)):
        if((pPath1 in pKeys) and (pPath1 in pKeys[pPath2])):
            pGraph[pPath1].append(pPath1)
    return pGraph

def generateMatrix(pGraph):
    valRen = [0] * (len(pGraph)**2)
    if(isinstance(pGraph, dict)):
        for key, listPath in pGraph.items():
            for val in listPath:
                valRen[key] = 1
    return valRen 


