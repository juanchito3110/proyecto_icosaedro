import pygame
import os
import random

class GestorTexturas:
    def __init__(self, ruta1="textura1.jpg", ruta2="textura2.jpg"):
        if not pygame.get_init():
            pygame.init()

        # Intenta cargar imágenes, si no existen, genera un patrón automático
        self.textura1 = self._cargar_o_generar(ruta1, (200,200), (180, 30, 120))
        self.textura2 = self._cargar_o_generar(ruta2, (200,200), (20, 120, 40))

    def _cargar_o_generar(self, ruta, tamaño, color_base):
        try:
            if os.path.exists(ruta):
                # Carga la imagen optimizada con alpha
                img = pygame.image.load(ruta).convert_alpha()
                return img
            else:
                # Generar un patrón simple (backup) si no existe el archivo jpg
                surf = pygame.Surface(tamaño, flags=pygame.SRCALPHA)
                surf.fill(color_base + (255,))
                w,h = tamaño
                # Dibuja líneas diagonales decorativas
                for i in range(0, w, 10):
                    pygame.draw.line(surf, (255,255,255,40), (i,0), (0,i), 2)

                for _ in range(80):
                    px = random.randint(0, w-1)
                    py = random.randint(0, h-1)
                    pygame.draw.circle(surf, (255,255,255,180), (px, py), random.randint(1,3))
                return surf
        except Exception:
            # En caso de error crítico, devuelve un gris neutro
            s = pygame.Surface(tamaño, flags=pygame.SRCALPHA)
            s.fill((150,150,150,255))
            return s

    def get_textura_para_indice(self, indice):
        # Alterna entre textura 1 y 2 dependiendo si la cara es par o impar
        return self.textura1 if (indice % 2 == 0) else self.textura2