# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 1

import sys
import math

# Función para comprobar si el piso actual tiene algún portal
def hasPortal(pisActual, portales):
    for i in portales:
        if (i[0] - 1) == pisActual:
            return True
    return False

# Función solución
def torreTp(pisActual, cuarActual, numPisos, numCuartos, numPortales, energia, portales):
    if pisActual == numPisos - 1:  # Caso base: si nos encontramos en el piso final
        return (numCuartos - 1 - cuarActual) * energia[pisActual]
    # Caso base: no hay portales en el piso actual (dicho camino no es solución)
    if not(hasPortal(pisActual, portales)):
        return math.inf

    # Variable iniciada en infinito que da el coste del camino con coste mínimo
    minimo = math.inf
    for i in portales:  # Se verifica cada portal en el piso actual y los caminos que salen de este de forma recursiva
        if i[0] - 1 == pisActual:
            coste = torreTp(i[2] - 1, i[3] - 1, numPisos, numCuartos, numPortales,
                            energia, portales) + (abs(cuarActual - (i[1] - 1))) * energia[pisActual]
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
        portales = []
        # Se consiguen los portales y se ingresan en la lista 'portales'
        for p in range(numPortales):
            portal = list(map(int, (input().split())))
            portales.append(portal)
        # Se llama a la función solución con los datos anteriores
        sol = torreTp(0, 0, numPisos, numCuartos,
                      numPortales, energia, portales)
        if sol == math.inf:  # Si el coste es infinito entonces la solución no existe
            solutions.append("NO EXISTE")
        else:  # Se agrega la solución a una lista de soluciones
            solutions.append(sol)

    # Output
    for i in solutions:
        print(i)


main()
