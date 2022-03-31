# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys
import math

# Función solución
def torreTp(numPisos, numCuartos, energia, portales, pisActual, cuarActual, costosMin):
    if pisActual == numPisos - 1:  # Caso base: si nos encontramos en el piso final
        return (numCuartos - 1 - cuarActual) * energia[pisActual]
    elif pisActual not in portales: # Caso base: no hay portales en el piso actual (dicho camino no es solución)
        return math.inf
    else:
        minimo = math.inf  # Variable iniciada en infinito que da el coste del camino con coste mínimo
        # Se verifica cada portal en el piso actual y los caminos que salen de este
        for portal in portales[pisActual]:
            portalKey = str(pisActual) + ',' + str(portal[0])
            if portalKey not in costosMin:
                costo = (torreTp(numPisos, numCuartos, energia, portales, portal[1], portal[2], costosMin) +
                        (abs(cuarActual - (portal[0]))) * energia[pisActual])
            else:
                costo = costosMin[portalKey]
            if costo == 0:
                return 0
            if costo < minimo:  # Se retorna el coste mínimo de todos estos posibles caminos
                minimo = costo
        return minimo


def main():
    input = sys.stdin.readline
    numberCases = int(input())  # Número de casos de prueba
    solutions = []
    for c in range(numberCases):
        data = list(map(int, (input().split())))
        numPisos, numCuartos, numPortales = data[0], data[1], data[2]
        energia, portales = list(map(int, (input().split()))), {}
        # Se consiguen los portales y se ingresan en la lista 'portales'
        for _ in range(numPortales):
            infoPortal = input().split()
            piso_i, cuarto_i, piso_f, cuarto_f = tuple(int(e) for e in infoPortal)
            if piso_i - 1 not in portales:
                portales[piso_i - 1] = []
            portales[piso_i - 1].append([cuarto_i - 1, piso_f - 1, cuarto_f - 1])
        # Se llama a la función solución con los datos anteriores
        sol = torreTp(numPisos, numCuartos, energia, portales, 0, 0, {})
        if sol == math.inf:  # Si el coste es infinito entonces la solución no existe
            solutions.append("NO EXISTE")
        else:  # Se agrega la solución a una lista de soluciones
            solutions.append(sol)
    # Output
    for i in solutions:
        print(i)


main()
