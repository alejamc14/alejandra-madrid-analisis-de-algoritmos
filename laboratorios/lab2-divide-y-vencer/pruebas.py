
"""Pruebas de los algoritmos de subarreglo maximo"""

import random

from subarreglo import (subarreglo_fuerza_bruta,subarreglo_maximo, suma_cruzada)


def verificar_resultado(valores: list[float]) -> None:
    """Comprueba que los dos algoritmos obtienen la misma suma"""
    resultado_bruto = subarreglo_fuerza_bruta(valores)
    resultado_divide = subarreglo_maximo(
        valores, 0, len(valores) - 1
    )

    assert resultado_bruto[2] == resultado_divide[2], (
        f"Resultados diferentes para {valores}: "
        f"{resultado_bruto} y {resultado_divide}"
    )

def suma_cruzada_prueba(valores: list[float]) -> float:
    """Devuelve la suma del mejor tramo cruzado del caso de prueba."""
    
    resultado = suma_cruzada(
        valores, 0, 1, len(valores) - 1
    )
    return resultado[2]


def main() -> None:
    """Ejecuta las pruebas requeridas."""
    # 1. Serie del enunciado: mejor suma igual a 17.
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]

    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(
        serie, 0, len(serie) - 1
    )[2] == 17

    # 2. Un solo elemento.
    verificar_resultado([7])
    assert subarreglo_maximo([7], 0, 0)[2] == 7

    # 3. Todos los elementos son negativos.
    negativos = [-8, -3, -6, -2, -9]
    verificar_resultado(negativos)
    assert subarreglo_maximo(
        negativos, 0, len(negativos) - 1
    )[2] == -2

    # 4. Todos los elementos son positivos.
    positivos = [2, 4, 1, 3]
    verificar_resultado(positivos)
    assert subarreglo_maximo(
        positivos, 0, len(positivos) - 1
    )[2] == 10

    # 5. El mejor tramo cruza el punto medio.
    cruzado = [4, -1, 5, 6]
    verificar_resultado(cruzado)
    assert suma_cruzada_prueba(cruzado) == 14

    # 6. Al menos veinte listas aleatorias reproducibles.
    generador = random.Random(42)

    for _ in range(30):
        cantidad = generador.randint(1, 30)
        valores = [
            generador.randint(-20, 20)
            for _ in range(cantidad)
        ]
        verificar_resultado(valores)

    print("Todas las pruebas finalizaron correctamente.")
    print("Casos fijos y 30 listas aleatorias verificados.")



if __name__ == "__main__":
    main()