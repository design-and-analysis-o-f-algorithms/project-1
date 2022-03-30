# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys
import math

#funciones
def hasPortal(pisActual, portales):
    for i in portales:
        if (i[0]-1)==pisActual:
            return True
    return False

def torreTp(pisActual, cuarActual,numPisos, numCuartos, numPortales, energia, portales):
    if pisActual==numPisos-1:
        return (numCuartos-1-cuarActual)*energia[pisActual]
    if not(hasPortal(pisActual, portales)):
        return math.inf

    minimo=math.inf
    for i in portales:
        if i[0]-1==pisActual:
            coste=torreTp(i[2]-1, i[3]-1, numPisos, numCuartos, numPortales, energia, portales)+(abs(cuarActual-(i[1]-1)))*energia[pisActual]
            if coste<minimo:
                minimo=coste
    return minimo

#input y llamado de funcion solucion
input = sys.stdin.readline
numberCases = int(input()) #Numero de casos de prueba
solutions=[]
for c in range(numberCases):
    data = list(map(int,(input().split())))
    numPisos=data[0]
    numCuartos=data[1]
    numPortales=data[2]
    energia = list(map(int,(input().split())))
    portales=[]
    for p in range(numPortales):
        portal = list(map(int,(input().split())))
        portales.append(portal)
    sol=torreTp(0,0,numPisos, numCuartos, numPortales, energia, portales)
    if sol==math.inf:
        solutions.append("NO EXISTE")
    else:
        solutions.append(sol)
        
# output
for i in solutions:
    print(i)