class Pixel:
    def __init__(self, ventana):
        self.ventana = ventana

    def getPixel(self, x, y): 
        if 0 <= x < self.ventana.get_width() and 0 <= y < self.ventana.get_height():
            return self.ventana.get_at((x, y))
        return (0, 0, 0, 0)
    
    def dibujar_pixel(self, x, y, color):
        x = int(round(x))
        y = int(round(y))

        try:
            r_o, g_o, b_o, a_o = color 
        except ValueError:
            # Si el color no tiene Alpha, opacidad total
            r_o, g_o, b_o = color
            a_o = 255 

        if a_o == 255:
            self.ventana.set_at((x, y), (r_o, g_o, b_o))
            return

        #obtener el color actual del píxel
        color_destino = self.getPixel(x, y)
        r_d, g_d, b_d, a_d = color_destino

        alpha = a_o / 255.0
        inv_alpha = 1.0 - alpha
        
        #Mezcla Alpha
        # Resultado = Origen * Alpha + Destino * (1 - Alpha)
        r_res = int(r_o * alpha + r_d * inv_alpha)
        g_res = int(g_o * alpha + g_d * inv_alpha)
        b_res = int(b_o * alpha + b_d * inv_alpha)
        
        # calcular el Alpha resultante 
        a_res = int(a_o + a_d * inv_alpha)

        # dibujar pixel mezclado
        r_res = min(255, max(0, r_res))
        g_res = min(255, max(0, g_res))
        b_res = min(255, max(0, b_res))
        a_res = min(255, max(0, a_res))

        self.ventana.set_at((x, y), (r_res, g_res, b_res, a_res))