"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break

        lista[j + 1] = clave

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2

    izquierda = datos[:mitad]
    derecha = datos[mitad:]

    izquierda_ordenada, comparaciones_izquierda = merge_sort(izquierda)
    derecha_ordenada, comparaciones_derecha = merge_sort(derecha)

    resultado = []
    i = 0
    j = 0
    comparaciones = (
        comparaciones_izquierda + comparaciones_derecha
    )

    while i < len(izquierda_ordenada) and j < len(derecha_ordenada):
        comparaciones += 1

        if izquierda_ordenada[i] >= derecha_ordenada[j]:
            resultado.append(izquierda_ordenada[i])
            i += 1
        else:
            resultado.append(derecha_ordenada[j])
            j += 1

    resultado.extend(izquierda_ordenada[i:])
    resultado.extend(derecha_ordenada[j:])

    return resultado, comparaciones
