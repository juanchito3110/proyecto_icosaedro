from pixel import Pixel


class DDA:
    def __init__(self, ventana):
        self.ventana = ventana
        self.pixel = Pixel(self.ventana)

    def dibujar_recta_DDA2(self, x1, y1, x2, y2, color):
        # 1. Calcular la diferencia entre puntos
        dy = (y2 - y1)
        dx = (x2 - x1)

        # Esto define si recorremos pixel por pixel en horizontal o vertical
        if abs(dx) > abs(dy):
            pasos = abs(dx)
        else:
            pasos = abs(dy)

        # Evitar división por cero si es el mismo punto
        if pasos == 0:
            self.pixel.dibujar_pixel(x1, y1, color)
            return

        # 3. Calcular incremento por paso (puede ser decimal)
        incrementoX = dx / pasos
        incrementoY = dy / pasos

        x = float(x1)
        y = float(y1)

        # 4. Ciclo para dibujar cada pixel de la línea
        for paso in range(int(pasos) + 1):
            # Se redondea porque los pixeles son enteros
            self.pixel.dibujar_pixel(round(x), round(y), color)
            x += incrementoX
            y += incrementoY