class Escalar3D:
    def __init__(self):
        pass

    def escalar_3D(self, vertices, Sx, Sy, Sz):
        """ Aumenta o disminuye el tamaño del objeto """
        coordenadasEscaladas = []
        for coordenadas in vertices:
            x, y, z = coordenadas
            matrizPuntoAEscalar = ([x], [y], [z], [1])

            # Matriz de Escalado: Sx, Sy, Sz van en la diagonal principal
            matrizIndentidad = ([Sx, 0, 0, 0],
                                [0, Sy, 0, 0],
                                [0, 0, Sz, 0],
                                [0, 0, 0, 1])

            matrizResultado = [[0], [0], [0], [0]]
            # Multiplicación manual
            for i in range(4):
                for j in range(1):
                    suma = 0
                    for k in range(4):
                        suma += matrizIndentidad[i][k] * matrizPuntoAEscalar[k][j]
                    matrizResultado[i][j] = suma

            coordenadasEscaladas.append((matrizResultado[0][0], matrizResultado[1][0], matrizResultado[2][0]))

        return coordenadasEscaladas