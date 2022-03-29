# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys

input = sys.stdin.readline
numberCases = int(input()) #Numero de casos de prueba

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
    

# IMPRESION
# for i in flips:
#     for j in i:
#         if (j==i[len(i)-1]):
#             print(j, end="")
#         else:
#             print (j, end =" ")
#     print("")