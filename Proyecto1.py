# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys
import math

#funciones
def hasPortal(pisActual, portales):#Funcion para comprobar si el piso actual tiene algun portal
    for i in portales:
        if (i[0]-1)==pisActual:
            return True
    return False

def torreTp(pisActual, cuarActual,numPisos, numCuartos, numPortales, energia, portales):#Funcion solucion
    if pisActual==numPisos-1:#Caso base: si nos encontramos en el piso final
        return (numCuartos-1-cuarActual)*energia[pisActual]
    if not(hasPortal(pisActual, portales)):#Caso base: no hay portales en el piso actual (dicho camino no es solucion)
        return math.inf

    minimo=math.inf#Variable iniciada en infinito que da el coste del camino con coste minimo
    for i in portales:#Se verifica cada portal en el piso actual y los caminos que salen de este de forma recursiva
        if i[0]-1==pisActual:
            coste=torreTp(i[2]-1, i[3]-1, numPisos, numCuartos, numPortales, energia, portales)+(abs(cuarActual-(i[1]-1)))*energia[pisActual]
            if coste<minimo:#Se retorna el coste minimo de todos estos posibles caminos
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
    for p in range(numPortales):#Se consiguen los portales y se ingresan en la lista 'portales'
        portal = list(map(int,(input().split())))
        portales.append(portal)
    sol=torreTp(0,0,numPisos, numCuartos, numPortales, energia, portales)#Se llama a la funcion solucion con los datos anteriores
    if sol==math.inf:#Si el coste es infinito entonces la solucion no existe
        solutions.append("NO EXISTE")
    else:#Se agrega la solucion a una lista de soluciones
        solutions.append(sol)
        
# output
for i in solutions:
    print(i)