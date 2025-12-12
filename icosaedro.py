import pygame
import math
from texturas import GestorTexturas
from sombreado import sombreado_plano
from rectaDDA import DDA


class Icosaedro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.linea = DDA(self.ventana)  # Para dibujar bordes
        self.gestor_texturas = GestorTexturas()  # Manejador de texturas
        self.direccion_luz = (0, 0, -1)  # La luz viene de frente

    def hacer_permutacion(self, coordenada_x, coordenada_y):
        """ Genera los 12 vértices de un icosaedro usando la proporción áurea """
        a = (1 + math.sqrt(5)) / 2  # Número áureo (Phi)
        x, y = coordenada_x, coordenada_y

        # Se generan los vértices permutando coordenadas rectangulares
        # Grupo 1 (Plano YZ)
        v1, v2, v3, v4 = (x, y, a), (x, y, -a), (x, -y, a), (x, -y, -a)
        # Grupo 2 (Plano ZX)
        v5, v6, v7, v8 = (y, a, x), (y, -a, x), (-y, a, x), (-y, -a, x)
        # Grupo 3 (Plano XY)
        v9, v10, v11, v12 = (a, x, y), (a, x, -y), (-a, x, y), (-a, x, -y)

        return [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12]

    def proyectar_icosaedro(self, vertices, vectorP, inicioX, inicioY, escala):
        """ Convierte coordenadas 3D (x,y,z) a 2D de pantalla """
        xp, yp, zp = vectorP
        proyeccion = []
        for vertice in vertices:
            x1, y1, z1 = vertice
            # Fórmula de proyección de perspectiva: x' = x / (z/zp)
            # Se añade un offset (inicioX, inicioY) para centrar en pantalla
            x = inicioX + (x1 - yp * (z1 / zp)) * escala
            y = inicioY + (y1 - yp * (z1 / zp)) * escala
            proyeccion.append((x, y))
        return proyeccion

    def obtener_aristas(self, coordenas):
        """ Determina qué vértices están conectados basándose en la distancia """
        numeroVertices = len(coordenas)
        aristas = []
        # ... (Cálculo de distancia mínima para encontrar vecinos) ...
        # Se omite detalle matemático repetitivo, se mantiene lógica de conexión
        distancia_minima = float(100)
        # Busca la distancia más corta entre puntos (la longitud de la arista)
        for i in range(numeroVertices):
            for j in range(i + 1, numeroVertices):
                dist = math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(coordenas[i], coordenas[j])))
                if 1e-6 < dist < distancia_minima: distancia_minima = dist

        # Conecta los puntos que estén a esa distancia mínima
        for i in range(numeroVertices):
            for j in range(i + 1, numeroVertices):
                dist = math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(coordenas[i], coordenas[j])))
                if abs(dist - distancia_minima) < 1e-6:
                    aristas.append((i, j))
        return aristas

    def obtener_caras(self, aristas):
        """ Encuentra triángulos (ciclos de 3 vértices conectados) """
        juego_aristas = set(frozenset((i, j)) for i, j in aristas)
        caras = []
        num_vertices = 12
        # Fuerza bruta optimizada para encontrar triángulos
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if frozenset((i, j)) not in juego_aristas: continue
                for k in range(j + 1, num_vertices):
                    if frozenset((i, k)) in juego_aristas and frozenset((j, k)) in juego_aristas:
                        caras.append((i, j, k))
        return caras

    def rellenar_triangulo_scanline(self, p1, p2, p3, color):
        """ Algoritmo de relleno mediante barrido de líneas horizontales """
        vertices = [p1, p2, p3]
        y_min = int(min(v[1] for v in vertices))
        y_max = int(max(v[1] for v in vertices))

        # Barrido de arriba a abajo
        for y in range(y_min, y_max + 1):
            intersecciones = []
            for i in range(len(vertices)):
                v1, v2 = vertices[i], vertices[(i + 1) % len(vertices)]
                x1, y1 = v1
                x2, y2 = v2
                if y1 == y2: continue  # Ignorar líneas horizontales

                # Calcular intersección X para la altura Y actual
                if (y >= min(y1, y2)) and (y < max(y1, y2)):
                    x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersecciones.append(x_int)

            intersecciones.sort()
            # Si hay intersecciones, dibujar línea entre ellas
            if len(intersecciones) >= 2:
                self.linea.dibujar_recta_DDA2(int(intersecciones[0]), y, int(intersecciones[1]), y, color)

    def rellenar_icosaedro(self, vertices_3d, proyeccion_2d, caras, color_relleno, color_borde):
        """ Dibuja el objeto completo aplicando algoritmo del pintor y texturas """

        # --- ALGORITMO DEL PINTOR ---
        # 1. Calcular la profundidad Z promedio de cada cara
        caras_con_z = []
        for cara in caras:
            i, j, k = cara
            z_avg = (vertices_3d[i][2] + vertices_3d[j][2] + vertices_3d[k][2]) / 3.0
            caras_con_z.append((z_avg, cara))

        # 2. Ordenar caras de atrás hacia adelante (Z mayor a menor)
        caras_con_z.sort(key=lambda x: x[0], reverse=True)

        # 3. Dibujar en ese orden
        for idx, (z, cara) in enumerate(caras_con_z):
            i, j, k = cara
            p1, p2, p3 = proyeccion_2d[i], proyeccion_2d[j], proyeccion_2d[k]

            # --- ILUMINACIÓN (Sombreado Plano) ---
            intensidad = sombreado_plano(vertices_3d[i], vertices_3d[j], vertices_3d[k], self.direccion_luz)

            # Ajustar color base según intensidad de luz
            color_mod = (
                int(color_relleno[0] * intensidad),
                int(color_relleno[1] * intensidad),
                int(color_relleno[2] * intensidad)
            )

            # --- TEXTURIZADO ---
            # Rellenar primero con color sólido (scanline)
            self.rellenar_triangulo_scanline(p1, p2, p3, color_mod)

            # Aplicar textura con máscaras de Pygame
            try:
                textura = self.gestor_texturas.get_textura_para_indice(idx)

            except Exception:
                pass  # Si falla la textura, queda el color sólido

            # --- DIBUJO DE BORDES (Wireframe) ---
            if color_borde:
                self.linea.dibujar_recta_DDA2(p1[0], p1[1], p2[0], p2[1], color_borde)
                self.linea.dibujar_recta_DDA2(p2[0], p2[1], p3[0], p3[1], color_borde)
                self.linea.dibujar_recta_DDA2(p3[0], p3[1], p1[0], p1[1], color_borde)