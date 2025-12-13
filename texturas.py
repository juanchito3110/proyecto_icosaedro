import pygame
import os
import random
from rectaDDA import DDA
from circuloCoordenadasPolaresConCentro import CirculoCoordenadasPolaresConCentro


class GestorTexturas:

    def __init__(self, ruta1="textura1.jpg", ruta2="textura2.jpg"):
        if not pygame.get_init():
            pygame.init()

        self.textura1 = self._cargar_o_generar(ruta1, (200, 200), (180, 30, 120))
        self.textura2 = self._cargar_o_generar(ruta2, (200, 200), (20, 120, 40))

    def _cargar_o_generar(self, ruta, tamaño, color_base):
        try:
            if os.path.exists(ruta):
                img = pygame.image.load(ruta).convert_alpha()
                return img
            else:
                # Generar un patrón simple si no existe el archivo
                surf = pygame.Surface(tamaño, flags=pygame.SRCALPHA)
                surf.fill(color_base + (255,))
                w, h = tamaño
                # líneas diagonales
                for i in range(0, w, 10):
                    linea = DDA(surf)
                    linea.dibujar_recta_DDA2(i, 0, 0, i, (255, 255, 255, 40))

                # pequeños puntos (copos)
                for _ in range(80):
                    px = random.randint(0, w - 1)
                    py = random.randint(0, h - 1)
                    circulo = CirculoCoordenadasPolaresConCentro(surf)
                    circulo.dibujar_circulo_coordenadas_polares_con_centro(px, py, random.randint(1, 3),
                                                                           (255, 255, 255, 180))
                return surf
        except Exception:
            # En caso de error, devolver una superficie neutra
            s = pygame.Surface(tamaño, flags=pygame.SRCALPHA)
            s.fill((150, 150, 150, 255))
            return s

    def get_textura_para_indice(self, indice):
        # Alterna texturas según el índice de la cara
        return self.textura1 if (indice % 2 == 0) else self.textura2