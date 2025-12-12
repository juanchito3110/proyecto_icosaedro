class Traslacion3D:
    def __init__(self):
        pass

    def trasladar_3D(self, vertices, tx, ty, tz):
        """ Aplica una matriz de traslación a cada vértice """
        coordenadasTrasladadas = []
        for coordenadas in vertices:
            x, y, z = coordenadas
            matrizPuntoATrasladar = ([x], [y], [z], [1])

            # Matriz de Traslación: Los valores tx, ty, tz van en la última columna
            matrizIndentidad = ([1, 0, 0, tx],
                                [0, 1, 0, ty],
                                [0, 0, 1, tz],
                                [0, 0, 0, 1])

            # Multiplicación de matrices para obtener nueva posición
            matrizResultado = [[0], [0], [0], [0]]
            for i in range(4):
                for j in range(1):
                    suma = 0
                    for k in range(4):
                        suma += matrizIndentidad[i][k] * matrizPuntoATrasladar[k][j]
                    matrizResultado[i][j] = suma

            coordenadasTrasladadas.append((matrizResultado[0][0], matrizResultado[1][0], matrizResultado[2][0]))
        return coordenadasTrasladadas