class Pixel:
    def __init__(self, ventana):
        self.ventana = ventana

    # Obtener el color de un pixel específico
    def getPixel(self, x, y):
        return self.ventana.get_at((x, y))

    # Dibujar un pixel individual en la pantalla
    def dibujar_pixel(self, x, y, color):
        # set_at requiere enteros, por eso usamos int(round())
        self.ventana.set_at((int(round(x)), int(round(y))), color)