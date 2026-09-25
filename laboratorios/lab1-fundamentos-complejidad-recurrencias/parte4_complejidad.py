"""
Experimento de la Parte 4.

Compara el tiempo de ejecución de Insertion Sort y Merge Sort
utilizando el escenario A (datos aleatorios).
"""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo de ejecución de un algoritmo de ordenamiento.

    Args:
        algoritmo: Función de ordenamiento que se desea medir.
        datos: Lista de datos sobre la que se ejecutará el algoritmo.

    Returns:
        Tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()

    algoritmo(datos)

    fin = time.perf_counter()

    return fin - inicio


def generar_grafica_tiempo(
    tiempos_insertion: list[float],
    tiempos_merge: list[float],
) -> None:
    """Genera y guarda la gráfica comparativa de tiempos.

    Args:
        tiempos_insertion: Tiempos obtenidos con Insertion Sort.
        tiempos_merge: Tiempos obtenidos con Merge Sort.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title(
        "Comparación de tiempo: Insertion Sort vs Merge Sort"
    )
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "laboratorios/lab1-fundamentos-complejidad-recurrencias/"
        "graficas/parte4_tiempo.png"
    )

    plt.close()


def main() -> None:
    """Ejecuta el experimento de comparación de tiempos."""

    tiempos_insertion = []
    tiempos_merge = []

    print()
    print("RESULTADOS DEL EXPERIMENTO - PARTE 4")
    print("=" * 80)

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_tiempo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_tiempo(
            merge_sort,
            datos,
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print()
        print(f"Tamaño de entrada: {n}")
        print(
            f"  Insertion Sort: "
            f"{tiempo_insertion:.6f} segundos"
        )
        print(
            f"  Merge Sort: "
            f"{tiempo_merge:.6f} segundos"
        )

    generar_grafica_tiempo(
        tiempos_insertion,
        tiempos_merge,
    )

    print()
    print("Gráfica generada correctamente:")
    print(
        "graficas/parte4_tiempo.png"
    )


if __name__ == "__main__":
    main()