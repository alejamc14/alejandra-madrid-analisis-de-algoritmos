
"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias.

    Args:
        valores: Variacion diaria de caja, con al menos un elemento.

    Returns:
        Una tupla con el indice inicial, final y la suma maxima.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for i in range(len(valores)):
        suma_actual = 0

        for j in range(i, len(valores)):
            suma_actual += valores[j]

            if suma_actual > mejor_suma:
                mejor_inicio = i
                mejor_fin = j
                mejor_suma = suma_actual

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha que cruza el punto medio.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango, inclusive.
        medio: Ultimo indice de la mitad izquierda.
        fin: Indice final del rango, inclusive.

    Returns:
        Una tupla con el inicio, el fin y la suma de la mejor racha
        que incluye elementos de ambas mitades.
    """
    suma_actual = 0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]

        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    suma_actual = 0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]

        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    suma_cruzada_maxima = (
        mejor_suma_izquierda + mejor_suma_derecha
    )

    return mejor_inicio, mejor_fin, suma_cruzada_maxima


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha usando divide y venceras.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango, inclusive.
        fin: Indice final del rango, inclusive.

    Returns:
        Una tupla con el inicio, el fin y la suma maxima.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzada = suma_cruzada(valores, inicio, medio, fin)

    mejor = izquierda

    if derecha[2] > mejor[2]:
        mejor = derecha

    if cruzada[2] > mejor[2]:
        mejor = cruzada

    return mejor