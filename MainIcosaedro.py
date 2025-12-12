import pygame
import sys
from icosaedro import Icosaedro
from escalar3D import Escalar3D
from rotacion3D import Rotacion3D
from traslacion3D import Traslacion3D
from rectaDDA import DDA

# --- INICIALIZACIÓN DE PYGAME ---
pygame.init()
ANCHO, ALTO = 1200, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Icosaedro - Proyecto 3er Parcial")

# Carga de fondo y ajuste de escala
fondito = pygame.transform.scale(pygame.image.load("fondo2.jpeg"), (1200, 620))

# --- DEFINICIÓN DE COLORES (RGB) ---
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (57, 255, 20)
ROSA = (255, 20, 147)
AMARILLO = (255, 255, 0)
AZUL = (0, 220, 255)

# --- INSTANCIAS DE CLASES DE TRANSFORMACIÓN ---
# Se crean los objetos que manejarán la geometría y las matemáticas
icosaedro = Icosaedro(ventana)
rotar3D = Rotacion3D()
escalar3D = Escalar3D()
trasladar3D = Traslacion3D()
linea = DDA(ventana)

# Variables de control del bucle principal
corriendo = True
tx, ty, tz = 0, 0, 0  # Variables de traslación
Sx, Sy, Sz = 1, 1, 1  # Variables de escalado
anguloRotacion = 0
vuelta = 0  # Contador para cambiar estados/colores

# Generación inicial de la geometría del icosaedro
coordenadas = icosaedro.hacer_permutacion(0, 1)  # Vértices
aristas = icosaedro.obtener_aristas(coordenadas)  # Conexiones
caras = icosaedro.obtener_caras(aristas)  # Superficies

# --- BUCLE PRINCIPAL (Game Loop) ---
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar fondo en cada frame para limpiar el anterior
    ventana.blit(fondito, (0, 0))

    # --- LÓGICA DE ROTACIÓN Y ESTADOS ---
    # Controla la velocidad de rotación y los cambios de ciclo (vuelta)
    anguloRotacion += 10
    if anguloRotacion >= 100:
        vuelta += 1
        if vuelta > 4: vuelta = 0  # Reinicia el ciclo
        anguloRotacion = 0

    # --- LÓGICA DE ESCALADO (Pulsación) ---
    # Hace que el objeto crezca hasta 1.5 y se reinicie
    if Sx < 1.5 and Sy < 1.5 and Sz < 1.5:
        Sx += .1
        Sy += .1
        Sz += .1
    else:
        Sx = 1.5
        Sy = 1.5
        Sz = 1.5

    # --- CAMBIO DE COLORES SEGÚN LA VUELTA ---
    if vuelta == 0:
        colorCara = ROJO;
        colorArista = BLANCO
    elif vuelta == 1:
        colorCara = VERDE;
        colorArista = NEGRO
    elif vuelta == 2:
        colorCara = AMARILLO;
        colorArista = NEGRO
    elif vuelta == 3:
        colorCara = ROSA;
        colorArista = BLANCO
    else:
        colorCara = AZUL;
        colorArista = BLANCO

    # Dibujar las cuerdas del "tendedero" usando algoritmo DDA
    linea.dibujar_recta_DDA2(0, 100, ANCHO, 100, NEGRO)
    linea.dibujar_recta_DDA2(0, 170, ANCHO, 170, NEGRO)

    # --- TRANSFORMACIONES Y RENDERIZADO ---

    # 1. Rotación: Se rota el modelo base
    coordenadasRotadas = rotar3D.rotarEjeY(coordenadas, anguloRotacion)

    # 2. Traslación y Proyección: Se mueve y se proyecta a 2D
    # Se reutiliza la lógica para dibujar múltiples icosaedros en diferentes posiciones X

    # --- TENDEDERO 1 (Fila superior) ---
    # Se dibujan múltiples esferas desplazando la coordenada X (primer parámetro de proyectar)
    posiciones_x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
    colores = [AMARILLO, VERDE, ROJO]  # Patrón de colores

    for i, pos_x in enumerate(posiciones_x):
        # Traslación (aunque aquí se maneja más en la proyección directa)
        coordenadasFinales = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)

        # Proyección: Convierte 3D a 2D.
        # Parámetros: coords, vector vista, PosX en pantalla, PosY en pantalla, Escala
        proyeccion = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], pos_x, 120, 10)

        # Relleno: Dibuja las caras ordenadas y texturizadas
        color_actual = colores[i % 3]  # Alterna colores
        borde_actual = BLANCO if color_actual == ROJO else NEGRO
        icosaedro.rellenar_icosaedro(coordenadasFinales, proyeccion, caras, color_actual, borde_actual)

    # --- TENDEDERO 2 (Fila inferior) ---
    # Repetimos el proceso para la segunda fila en Y = 190
    for i, pos_x in enumerate(posiciones_x):
        coordenadasFinales = trasladar3D.trasladar_3D(coordenadasRotadas, tx, ty, tz)
        proyeccion = icosaedro.proyectar_icosaedro(coordenadasFinales, [1, 1, 2], pos_x, 190, 10)

        # Invertimos patrón de colores para variar
        color_actual = colores[(i + 1) % 3]
        borde_actual = BLANCO if color_actual == ROJO else NEGRO
        icosaedro.rellenar_icosaedro(coordenadasFinales, proyeccion, caras, color_actual, borde_actual)

    # Actualizar pantalla
    pygame.display.update()

pygame.quit()
sys.exit()