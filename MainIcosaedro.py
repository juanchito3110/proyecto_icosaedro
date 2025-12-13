import pygame
import sys

from icosaedro import Icosaedro
from escalar3D import Escalar3D
from rotacion3D import Rotacion3D
from traslacion3D import Traslacion3D
from rectaDDA import DDA

# inicializar
pygame.init()
ANCHO, ALTO = 1200, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Icosaedro")
fondito = pygame.transform.scale(pygame.image.load("fondo2.jpeg"), (1200, 620))

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
MORADO = (128, 0, 128)
BLANCO = (255, 255, 255)
VERDE = (57, 255, 20)
ROSA = (255, 20, 147)
AZUL = (0, 220, 255)
AMARILLO = (255, 255, 0)

# Instancia de la clase
icosaedro = Icosaedro(ventana)
rotar3D = Rotacion3D()
escalar3D = Escalar3D()
trasladar3D = Traslacion3D()
linea = DDA(ventana)

corriendo = True
dx = 0
dy = 0
tx = 0
ty = 0
tz = 0
Sx = 1
Sy = 1
Sz = 1
anguloRotacion = 0
estado = "rotaciónZ"
vuelta = 0

coordenadas = icosaedro.hacer_permutacion(0, 1)
aristas = icosaedro.obtener_aristas(coordenadas)
caras = icosaedro.obtener_caras(aristas)
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.blit(fondito, (0, 0))
    # ventana.fill(AZUL)

    anguloRotacion += 10
    if vuelta == 0:
        if anguloRotacion >= 100:
            vuelta = 1
            anguloRotacion = 0
    elif vuelta == 1:
        anguloRotacion += 10
        if anguloRotacion >= 100:
            vuelta = 2
            anguloRotacion = 0
    elif vuelta == 2:
        anguloRotacion += 10
        if anguloRotacion >= 100:
            vuelta = 3
            anguloRotacion = 0
    elif vuelta == 3:
        anguloRotacion += 10
        if anguloRotacion >= 100:
            vuelta = 4
            anguloRotacion = 0

    if Sx < 1.5 and Sy < 1.5 and Sz < 1.5:
        Sx += .1
        Sy += .1
        Sz += .1
    else:
        Sx = 1.5
        Sy = 1.5
        Sz = 1.5

    if vuelta == 0:
        colorCara = ROJO
        colorArista = BLANCO
    elif vuelta == 1:
        colorCara = VERDE
        colorArista = NEGRO
    elif vuelta == 2:
        colorCara = AMARILLO
        colorArista = NEGRO
    elif vuelta == 3:
        colorCara = ROSA
        colorArista = BLANCO

    linea.dibujar_recta_DDA2(0, 100, ANCHO, 100, NEGRO)
    linea.dibujar_recta_DDA2(0, 170, ANCHO, 170, NEGRO)
    # triangulito.dibujar_triángulo(base, VERDE)

    coordenadasRotadas = rotar3D.rotarEjeY(coordenadas, anguloRotacion)

    coordenadasFinales = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 580, 400, 80)
    icosaedro.rellenar_icosaedro(coordenadasFinales, proyeccion, caras, colorCara, colorArista)
    #########TENDEDERO 1
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 100, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, AMARILLO, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 200, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 300, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)
    #########
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 400, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, AMARILLO, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 500, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 600, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)
    #######
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 700, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, AMARILLO, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 800, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 900, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)
    #######
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 1000, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, AMARILLO, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 1100, 120, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, VERDE, NEGRO)

    #########TENDEDERO 2
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 100, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 200, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 300, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, AMARILLO, NEGRO)
    #####
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 400, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 500, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 600, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, AMARILLO, NEGRO)
    #######
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 700, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 800, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 900, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, AMARILLO, NEGRO)
    #######
    coordenadasEsfera1 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 1000, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera1, proyeccion1, caras, VERDE, NEGRO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 1100, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, ROJO, BLANCO)

    coordenadasEsfera2 = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
    proyeccion1 = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], 1200, 190, 10)
    icosaedro.rellenar_icosaedro(coordenadasEsfera2, proyeccion1, caras, AMARILLO, NEGRO)

    pygame.display.update()
pygame.quit()
sys.exit()