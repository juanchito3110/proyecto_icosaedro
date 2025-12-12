import math


def sombreado_plano(v1, v2, v3, direccion_luz=(0, 0, -1)):
    """ Calcula la intensidad de luz de una cara basándose en su normal """

    # 1. Calcular vectores del triángulo (Aristas)
    ux, uy, uz = v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]
    vx, vy, vz = v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]

    # 2. Calcular vector Normal (Producto Cruz)
    # La normal es perpendicular a la superficie de la cara
    nx = uy * vz - uz * vy
    ny = uz * vx - ux * vz
    nz = ux * vy - uy * vx

    # 3. Normalizar el vector (hacer que su longitud sea 1)
    mag_n = math.sqrt(nx * nx + ny * ny + nz * nz)
    if mag_n == 0: return 0.2
    nx, ny, nz = nx / mag_n, ny / mag_n, nz / mag_n

    # 4. Normalizar vector de luz
    lx, ly, lz = direccion_luz
    mag_l = math.sqrt(lx * lx + ly * ly + lz * lz)
    lx, ly, lz = lx / mag_l, ly / mag_l, lz / mag_l

    # 5. Producto Punto (Dot Product)
    # Determina qué tan alineada está la cara con la luz
    intensidad = nx * lx + ny * ly + nz * lz

    # Clampear valor (que no sea negativo)
    if intensidad < 0: intensidad = 0.0

    # Retornar intensidad con luz ambiental mínima (0.2)
    return 0.2 + 0.8 * intensidad