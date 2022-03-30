# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys
import math

# Función solución
def torreTp(pisActual, cuarActual, numPisos, numCuartos, numPortales, energia, portales):
    if pisActual == numPisos - 1:  # Caso base: si nos encontramos en el piso final
        return (numCuartos - 1 - cuarActual) * energia[pisActual]
    # Caso base: no hay portales en el piso actual (dicho camino no es solución)
    if pisActual not in portales:
        return math.inf

    # Variable iniciada en infinito que da el coste del camino con coste mínimo
    minimo = math.inf
    # Se verifica cada portal en el piso actual y los caminos que salen de este
    for portal in portales[pisActual]:
            coste = torreTp(portal[1], portal[2], numPisos, numCuartos, numPortales, energia, portales) + \
                    (abs(cuarActual - (portal[0]))) * energia[pisActual]
            if coste == 0:
                return 0  
            if coste < minimo:  # Se retorna el coste mínimo de todos estos posibles caminos
                minimo = coste
    return minimo


def main():
    # Input y llamado de función solución
    input = sys.stdin.readline
    numberCases = int(input())  # Numero de casos de prueba
    solutions = []
    for c in range(numberCases):
        data = list(map(int, (input().split())))
        numPisos = data[0]
        numCuartos = data[1]
        numPortales = data[2]
        energia = list(map(int, (input().split())))
        portales = {}
        # Se consiguen los portales y se ingresan en la lista 'portales'
        for _ in range(numPortales):
            infoPortal = input().split()
            piso_i, cuarto_i, piso_f, cuarto_f = tuple(int(e) for e in infoPortal)
            if piso_i - 1 not in portales:
                portales[piso_i - 1] = []
            portales[piso_i - 1].append([cuarto_i - 1, piso_f - 1, cuarto_f - 1])
        # Se llama a la función solución con los datos anteriores
        sol = torreTp(0, 0, numPisos, numCuartos, numPortales, energia, portales)
        if sol == math.inf:  # Si el coste es infinito entonces la solución no existe
            solutions.append("NO EXISTE")
        else:  # Se agrega la solución a una lista de soluciones
            solutions.append(sol)

    # Output
    for i in solutions:
        print(i)


main()
