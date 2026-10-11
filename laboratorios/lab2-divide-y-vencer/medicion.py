
"""Experimento de tiempos para el subarreglo maximo."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000]
SEMILLA = 42
REPETICIONES = 3


def medir_fuerza_bruta(valores: list[int],repeticiones: int) -> float:

    """Devuelve el tiempo promedio de fuerza bruta en segundos."""
    tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        subarreglo_fuerza_bruta(valores)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)


def medir_divide_y_venceras(valores: list[int], repeticiones: int) -> float:

    """Devuelve el tiempo promedio de divide y venceras."""
    tiempos = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        subarreglo_maximo(valores, 0, len(valores) - 1)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)


def crear_grafica(tamanos: list[int], tiempos_fuerza_bruta: list[float], tiempos_divide: list[float]) -> None:

    """Genera y guarda la grafica de tiempos en funcion de n."""
    carpeta_graficas = (
        Path(__file__).resolve().parent / "graficas"
    )
    carpeta_graficas.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))

    plt.plot(tamanos,tiempos_fuerza_bruta,marker="o",label="Fuerza bruta O(n²)")

    plt.plot(tamanos,tiempos_divide, marker="s",label="Divide y vencerás O(n log n)")

    plt.title("Comparación de tiempos: subarreglo máximo")
    plt.xlabel("Tamaño de entrada (n elementos)")
    plt.ylabel("Tiempo promedio de ejecución (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta_grafica = carpeta_graficas / "tiempo_vs_n.png"
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()

    print(f"\nGrafica guardada en: {ruta_grafica}")


def ejecutar_experimento() -> None:
    """Mide ambos algoritmos y guarda sus resultados."""
    generador = random.Random(SEMILLA)

    tiempos_fuerza_bruta = []
    tiempos_divide = []

    print("RESULTADOS DEL EXPERIMENTO")
    print("=" * 60)

    for n in TAMANOS:
        valores = [
            generador.randint(-100, 100)
            for _ in range(n)
        ]

        resultado_bruto = subarreglo_fuerza_bruta(valores)
        resultado_divide = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )

        assert resultado_bruto[2] == resultado_divide[2], (
            f"Las sumas no coinciden para n={n}: "
            f"{resultado_bruto[2]} y {resultado_divide[2]}"
        )

        tiempo_bruto = medir_fuerza_bruta(
            valores, REPETICIONES
        )
        tiempo_divide = medir_divide_y_venceras(
            valores, REPETICIONES
        )

        tiempos_fuerza_bruta.append(tiempo_bruto)
        tiempos_divide.append(tiempo_divide)

        print(f"\nTamaño de entrada: {n}")
        print(f"  Fuerza bruta: {tiempo_bruto:.8f} segundos")
        print(f"  Divide y venceras: {tiempo_divide:.8f} segundos")
        print(f"  Suma maxima: {resultado_bruto[2]}")

    crear_grafica(TAMANOS,tiempos_fuerza_bruta,tiempos_divide)


if __name__ == "__main__":
    ejecutar_experimento()
