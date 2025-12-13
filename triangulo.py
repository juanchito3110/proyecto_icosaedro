from rectaDDA import DDA

class Triangulo:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.linea = DDA(self.ventana) 

    def rellenar_scanline(self, p1, p2, p3, color):
        vertices = [p1, p2, p3]
        
        # Obtener los límites Y
        y_min = int(min(v[1] for v in vertices))
        y_max = int(max(v[1] for v in vertices))

        for y in range(y_min, y_max + 1):
            intersecciones = []
            
            # Calcular intersecciones con las 3 aristas
            for i in range(len(vertices)):
                v1 = vertices[i]
                v2 = vertices[(i + 1) % len(vertices)] 
                x1, y1 = v1
                x2, y2 = v2
                
                if y1 == y2: continue # linea horizontal
                
                # ver si la línea de escaneo esté entre y1 y y2
                if (y >= min(y1, y2)) and (y < max(y1, y2)):
                    try:
                        x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                        intersecciones.append(x_int)
                    except ZeroDivisionError:
                        continue 

            intersecciones.sort()
            
            # dibujar linea horizontal entre las dos intersecciones
            if len(intersecciones) >= 2:
                x_inicio = int(intersecciones[0])
                x_fin = int(intersecciones[1])
                
                if x_inicio < x_fin: 
                    self.linea.dibujar_recta_DDA2(x_inicio, y, x_fin, y, color)


    def dibujar_triángulo(self, vertices, color, rellenar=True):
        x1, y1 = vertices[0] 
        x2, y2 = vertices[1] 
        x3, y3 = vertices[2] 

        #si se quiere relleno
        if rellenar:
            self.rellenar_scanline(vertices[0], vertices[1], vertices[2], color)
        
        # Dibujar bordes
        self.linea.dibujar_recta_DDA2(x1, y1, x3, y3, color)
        self.linea.dibujar_recta_DDA2(x3, y3, x2, y2, color)
        self.linea.dibujar_recta_DDA2(x2, y2, x1, y1, color)