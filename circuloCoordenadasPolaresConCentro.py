from pixel import Pixel
from rectaDDA import DDA
import math
class CirculoCoordenadasPolaresConCentro:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.pixel = Pixel(self.ventana)
        self.linea = DDA(self.ventana) 

    def dibujar_circulo_coordenadas_polares_con_centro(self, centroX, centroY, radio, color):
        
        # Iterar sobre todos los ángulos 0-360
        for i in range(0, 360):
            anguloRadianes = math.radians(i)
            
            # Coordenadas 
            puntoX = centroX + radio * math.cos(anguloRadianes)
            puntoY = centroY + radio * math.sin(anguloRadianes)
            
            # Dibujar una línea
            self.linea.dibujar_recta_DDA2(centroX, centroY, puntoX, puntoY, color)
            