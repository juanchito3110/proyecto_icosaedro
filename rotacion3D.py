import math


class Rotacion3D:
    def __init__(self):
        pass

    # --- ROTACIÓN EN EJE X ---
    def rotarEjeX(self, vertices, angulo):
        coordenadasRotadas = []
        anguloRadianes = math.radians(angulo)  # Python usa radianes, no grados

        for coordenadas in vertices:
            x, y, z = coordenadas
            matrizPuntoARotar = ([x], [y], [z], [1])
            # Matriz de rotación X: Mantiene X, altera Y y Z
            matrizIndentidad = ([1, 0, 0, 0],
                                [0, math.cos(anguloRadianes), math.sin(anguloRadianes), 0],
                                [0, -math.sin(anguloRadianes), math.cos(anguloRadianes), 0],
                                [0, 0, 0, 1])

            # Multiplicación de matrices manual
            matrizResultado = [[0], [0], [0], [0]]
            for i in range(4):
                for j in range(1):
                    suma = 0
                    for k in range(4):
                        suma += matrizIndentidad[i][k] * matrizPuntoARotar[k][j]
                    matrizResultado[i][j] = suma

            coordenadasRotadas.append((matrizResultado[0][0], matrizResultado[1][0], matrizResultado[2][0]))
        return coordenadasRotadas

    # --- ROTACIÓN EN EJE Y ---
    def rotarEjeY(self, vertices, angulo):
        coordenadasRotadas = []
        anguloRadianes = math.radians(angulo)

        for coordenadas in vertices:
            x, y, z = coordenadas
            matrizPuntoARotar = ([x], [y], [z], [1])
            # Matriz de rotación Y: Mantiene Y, altera X y Z
            matrizIndentidad = (
                [math.cos(anguloRadianes), 0, -math.sin(anguloRadianes), 0],
                [0, 1, 0, 0],
                [math.sin(anguloRadianes), 0, math.cos(anguloRadianes), 0],
                [0, 0, 0, 1])

            # Multiplicación
            matrizResultado = [[0], [0], [0], [0]]
            for i in range(4):
                for j in range(1):
                    suma = 0
                    for k in range(4):
                        suma += matrizIndentidad[i][k] * matrizPuntoARotar[k][j]
                    matrizResultado[i][j] = suma

            coordenadasRotadas.append((matrizResultado[0][0], matrizResultado[1][0], matrizResultado[2][0]))
        return coordenadasRotadas

    # --- ROTACIÓN EN EJE Z ---
    def rotarEjeZ(self, vertices, angulo):
        coordenadasRotadas = []
        anguloRadianes = math.radians(angulo)
        for coordenadas in vertices:
            x, y, z = coordenadas
            matrizPuntoARotar = ([x], [y], [z], [1])
            # Matriz de rotación Z: Mantiene Z, altera X y Y
            matrizIndentidad = (
                [math.cos(anguloRadianes), math.sin(anguloRadianes), 0, 0],
                [-math.sin(anguloRadianes), math.cos(anguloRadianes), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1])

            # Multiplicación
            matrizResultado = [[0], [0], [0], [0]]
            for i in range(4):
                for j in range(1):
                    suma = 0
                    for k in range(4):
                        suma += matrizIndentidad[i][k] * matrizPuntoARotar[k][j]
                    matrizResultado[i][j] = suma

            coordenadasRotadas.append((matrizResultado[0][0], matrizResultado[1][0], matrizResultado[2][0]))
        return coordenadasRotadas