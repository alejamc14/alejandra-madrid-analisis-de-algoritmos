"""
Experimento de peor caso, mejor caso y caso promedio para insertion sort.

Este archivo ejecuta insertion sort sobre los tres escenarios de entrada
definidos para el caso Tamiza: aleatorio, casi ordenado y orden inverso.

Para cada escenario se prueban diferentes tamaños de entrada y se registran
el tiempo de ejecución y el número de comparaciones entre elementos.
Finalmente, se generan dos gráficas y se guardan en la carpeta graficas/.
"""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


# Tamaños de entrada utilizados para realizar el experimento.
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(generador, tamanos):
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        generador: Función utilizada para generar los datos de entrada.
        tamanos: Lista con los tamaños de entrada que se van a probar.

    Returns:
        Una tupla con dos listas:
        - tiempos de ejecución en segundos.
        - cantidad de comparaciones realizadas.
    """
    tiempos = []
    comparaciones = []

    for n in tamanos:
        # Los datos se generan antes de iniciar el cronómetro.
        # De esta manera no se mide el tiempo utilizado para generarlos.
        datos = generador(n)

        inicio = time.perf_counter()

        _, cantidad_comparaciones = insertion_sort(datos)

        fin = time.perf_counter()

        tiempo = fin - inicio

        tiempos.append(tiempo)
        comparaciones.append(cantidad_comparaciones)

    return tiempos, comparaciones


def imprimir_resultados(
    tamanos,
    tiempos_a,
    comparaciones_a,
    tiempos_b,
    comparaciones_b,
    tiempos_c,
    comparaciones_c,
):
    """Muestra en consola los resultados obtenidos en el experimento.

    Args:
        tamanos: Lista de tamaños de entrada.
        tiempos_a: Tiempos del escenario A.
        comparaciones_a: Comparaciones del escenario A.
        tiempos_b: Tiempos del escenario B.
        comparaciones_b: Comparaciones del escenario B.
        tiempos_c: Tiempos del escenario C.
        comparaciones_c: Comparaciones del escenario C.
    """
    print("\nRESULTADOS DEL EXPERIMENTO - PARTE 3")
    print("=" * 90)

    for i, n in enumerate(tamanos):
        print(f"\nTamaño de entrada: {n}")
        print(
            f"  Escenario A - Aleatorio: "
            f"{comparaciones_a[i]} comparaciones, "
            f"{tiempos_a[i]:.6f} segundos"
        )
        print(
            f"  Escenario B - Casi ordenado: "
            f"{comparaciones_b[i]} comparaciones, "
            f"{tiempos_b[i]:.6f} segundos"
        )
        print(
            f"  Escenario C - Inverso: "
            f"{comparaciones_c[i]} comparaciones, "
            f"{tiempos_c[i]:.6f} segundos"
        )


def generar_grafica_comparaciones(
    tamanos,
    comparaciones_a,
    comparaciones_b,
    comparaciones_c,
):
    """Genera la gráfica de comparaciones contra tamaño de entrada.

    Args:
        tamanos: Lista de tamaños de entrada.
        comparaciones_a: Comparaciones del escenario A.
        comparaciones_b: Comparaciones del escenario B.
        comparaciones_c: Comparaciones del escenario C.
    """
    plt.figure()

    plt.plot(
        tamanos,
        comparaciones_a,
        marker="o",
        label="Escenario A - Aleatorio",
    )

    plt.plot(
        tamanos,
        comparaciones_b,
        marker="o",
        label="Escenario B - Casi ordenado",
    )

    plt.plot(
        tamanos,
        comparaciones_c,
        marker="o",
        label="Escenario C - Orden inverso",
    )

    plt.title(
        "Insertion Sort: comparaciones según el tamaño de entrada"
    )
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)

    plt.savefig(
    "laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_comparaciones.png")
    plt.close()


def generar_grafica_tiempo(
    tamanos,
    tiempos_a,
    tiempos_b,
    tiempos_c,
):
    """Genera la gráfica de tiempo contra tamaño de entrada.

    Args:
        tamanos: Lista de tamaños de entrada.
        tiempos_a: Tiempos del escenario A.
        tiempos_b: Tiempos del escenario B.
        tiempos_c: Tiempos del escenario C.
    """
    plt.figure()

    plt.plot(
        tamanos,
        tiempos_a,
        marker="o",
        label="Escenario A - Aleatorio",
    )

    plt.plot(
        tamanos,
        tiempos_b,
        marker="o",
        label="Escenario B - Casi ordenado",
    )

    plt.plot(
        tamanos,
        tiempos_c,
        marker="o",
        label="Escenario C - Orden inverso",
    )

    plt.title(
        "Insertion Sort: tiempo de ejecución según el tamaño de entrada"
    )
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
    "laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_tiempo.png")
    plt.close()


def main():
    """Ejecuta el experimento completo de la Parte 3."""
    # Se ejecuta el experimento para cada uno de los tres escenarios.
    tiempos_a, comparaciones_a = medir_escenario(
        generar_aleatorio,
        TAMANOS,
    )

    tiempos_b, comparaciones_b = medir_escenario(
        generar_casi_ordenado,
        TAMANOS,
    )

    tiempos_c, comparaciones_c = medir_escenario(
        generar_inverso,
        TAMANOS,
    )

    # Se muestran los resultados obtenidos en la consola.
    imprimir_resultados(
        TAMANOS,
        tiempos_a,
        comparaciones_a,
        tiempos_b,
        comparaciones_b,
        tiempos_c,
        comparaciones_c,
    )

    # Se generan y guardan las dos gráficas solicitadas.
    generar_grafica_comparaciones(
        TAMANOS,
        comparaciones_a,
        comparaciones_b,
        comparaciones_c,
    )

    generar_grafica_tiempo(
        TAMANOS,
        tiempos_a,
        tiempos_b,
        tiempos_c,
    )

    print("\nGráficas generadas correctamente:")
    print("graficas/parte3_comparaciones.png")
    print("graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()