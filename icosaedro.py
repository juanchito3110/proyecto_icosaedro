import pygame
import math
from texturas import GestorTexturas
from sombreado import sombreado_plano
from triangulo import Triangulo

from rectaDDA import DDA


class Icosaedro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.linea = DDA(self.ventana)

        # Cargar Texturas 1 y 2
        self.gestor_texturas = GestorTexturas()
        # Dirección de la luz
        self.direccion_luz = (0, 0, -1)

    def hacer_permutacion(self, coordenada_x, coordenada_y):
        a = (1 + math.sqrt(5)) / 2
        x = coordenada_x
        y = coordenada_y

        # Permutación 1
        vertice1 = (x, y, a)
        vertice2 = (x, y, -a)
        vertice3 = (x, -y, a)
        vertice4 = (x, -y, -a)
        # Permutación 2
        vertice5 = (y, a, x)
        vertice6 = (y, -a, x)
        vertice7 = (-y, a, x)
        vertice8 = (-y, -a, x)
        # Permutacion 3
        vertice9 = (a, x, y)
        vertice10 = (a, x, -y)
        vertice11 = (-a, x, y)
        vertice12 = (-a, x, -y)

        verticesTotales = [vertice1, vertice2, vertice3,
                           vertice4, vertice5, vertice6,
                           vertice7, vertice8, vertice9,
                           vertice10, vertice11, vertice12]

        return verticesTotales

    def proyectar_icosaedro(self, vertices, vectorP, inicioX, inicioY, escala):
        xp, yp, zp = vectorP
        proyeccion = []
        for vertice in vertices:
            x1, y1, z1 = vertice
            x = inicioX + (x1 - yp * (z1 / zp)) * escala
            y = inicioY + (y1 - yp * (z1 / zp)) * escala
            proyeccion.append((x, y))

        return proyeccion

    def obtener_aristas(self, coordenas):

        numeroVertices = len(coordenas)
        aristas = []
        distancia_minima = float(100)
        tolerancia = 1e-6
        for i in range(numeroVertices):
            for j in range(i + 1, numeroVertices):
                x1, y1, z1 = coordenas[i]
                x2, y2, z2 = coordenas[j]
                distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
                if 1e-6 < distancia < distancia_minima:
                    distancia_minima = distancia

        largo_arista = distancia_minima
        for i in range(numeroVertices):
            for j in range(i + 1, numeroVertices):
                x1, y1, z1 = coordenas[i]
                x2, y2, z2 = coordenas[j]
                distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
                if abs(distancia - largo_arista) < tolerancia:
                    aristas.append((i, j))
        # print(len(aristas))
        return aristas

    def dibujar_icosaedro(self, proyeccion, aristas, color):

        for arista in aristas:
            # indices de la arista
            indiceX1 = arista[0]
            indiceX2 = arista[1]
            # coordenadas de los puntos
            p1 = proyeccion[indiceX1]
            p2 = proyeccion[indiceX2]

            self.linea.dibujar_recta_DDA2(p1[0], p1[1], p2[0], p2[1], color)

    def obtener_caras(self, aristas):

        juego_aristas = set()
        for i, j in aristas:
            juego_aristas.add(frozenset((i, j)))

        caras = []
        num_vertices = 12

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if frozenset((i, j)) not in juego_aristas:
                    continue
                for k in range(j + 1, num_vertices):
                    if frozenset((i, k)) in juego_aristas and frozenset((j, k)) in juego_aristas:
                        caras.append((i, j, k))

        return caras

    def rellenar_triangulo_scanline(self, p1, p2, p3, color):

        vertices = [p1, p2, p3]

        y_min = int(min(v[1] for v in vertices))
        y_max = int(max(v[1] for v in vertices))

        for y in range(y_min, y_max + 1):
            intersecciones = []
            for i in range(len(vertices)):
                v1 = vertices[i]
                v2 = vertices[(i + 1) % len(vertices)]
                x1, y1 = v1
                x2, y2 = v2
                if y1 == y2:
                    continue

                if (y >= min(y1, y2)) and (y < max(y1, y2)):
                    try:
                        x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                        intersecciones.append(x_int)
                    except ZeroDivisionError:
                        continue

            intersecciones.sort()

            if len(intersecciones) >= 2:
                x_inicio = int(intersecciones[0])
                x_fin = int(intersecciones[1])

                if x_inicio < x_fin:
                    self.linea.dibujar_recta_DDA2(x_inicio, y, x_fin, y, color)

    def rellenar_icosaedro(self, vertices_3d, proyeccion_2d, caras, color_relleno, color_borde):

        caras_con_z = []
        for cara in caras:
            i, j, k = cara
            v1_z = vertices_3d[i][2]
            v2_z = vertices_3d[j][2]
            v3_z = vertices_3d[k][2]
            z_avg = (v1_z + v2_z + v3_z) / 3.0
            caras_con_z.append((z_avg, cara))

        caras_con_z.sort(key=lambda x: x[0], reverse=True)

        # Recorremos con índice para alternar texturas
        for idx, (z, cara) in enumerate(caras_con_z):
            i, j, k = cara

            p1 = proyeccion_2d[i]
            p2 = proyeccion_2d[j]
            p3 = proyeccion_2d[k]

            #  intensidad del sombreado
            intensidad = sombreado_plano(vertices_3d[i], vertices_3d[j], vertices_3d[k], self.direccion_luz)
            try:
                color_mod = (
                    max(0, min(255, int(color_relleno[0] * intensidad))),
                    max(0, min(255, int(color_relleno[1] * intensidad))),
                    max(0, min(255, int(color_relleno[2] * intensidad)))
                )
            except Exception:
                # Queda igual en caso de no ser RGB
                color_mod = color_relleno

            textura = self.gestor_texturas.get_textura_para_indice(
                idx)  # Se aplica textura alternando el incide para no repetir caras

            xs = [p1[0], p2[0], p3[0]]
            ys = [p1[1], p2[1], p3[1]]
            min_x = int(min(xs))
            min_y = int(min(ys))
            max_x = int(max(xs))
            max_y = int(max(ys))
            w = max(1, max_x - min_x)
            h = max(1, max_y - min_y)

            # Rellenamos   con scanline
            self.rellenar_triangulo_scanline(p1, p2, p3, color_mod)

            # para aplicar la textura de acuerdo al tamaño del triangulo
            try:
                surf = pygame.Surface((w, h), flags=pygame.SRCALPHA)
                surf.fill((0, 0, 0, 0))

                tex_scaled = pygame.transform.smoothscale(textura, (w, h))
                tex_scaled = tex_scaled.convert_alpha() if hasattr(tex_scaled, "convert_alpha") else tex_scaled
                surf.blit(tex_scaled, (0, 0))

                mask_surf = pygame.Surface((w, h), flags=pygame.SRCALPHA)
                mask_surf.fill((0, 0, 0, 0))  # transparente
                rel_p1 = (int(p1[0] - min_x), int(p1[1] - min_y))
                rel_p2 = (int(p2[0] - min_x), int(p2[1] - min_y))
                rel_p3 = (int(p3[0] - min_x), int(p3[1] - min_y))
                triangulo = Triangulo(mask_surf)
                triangulo.dibujar_triángulo([rel_p1, rel_p2, rel_p3], (255, 255, 255, 255))
                # pygame.draw.polygon(mask_surf, (255,255,255,255), [rel_p1, rel_p2, rel_p3])

                surf.blit(mask_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                shade = pygame.Surface((w, h), flags=pygame.SRCALPHA)
                shade.fill((color_mod[0], color_mod[1], color_mod[2], 255))
                surf.blit(shade, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                # manejamos transparenias para evitar los cuadros negros
                self.ventana.blit(surf, (min_x, min_y))
            except Exception as e:
                # Si algo falla con la textura, solo dejamos el triángulo coloreado con scanline
                pass

            # bordes definidos
            if color_borde:
                self.linea.dibujar_recta_DDA2(p1[0], p1[1], p2[0], p2[1], color_borde)
                self.linea.dibujar_recta_DDA2(p2[0], p2[1], p3[0], p3[1], color_borde)
                self.linea.dibujar_recta_DDA2(p3[0], p3[1], p1[0], p1[1], color_borde)