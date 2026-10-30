
"""Experimentos de rendimiento para lista enlazada y tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


# Ruta de la carpeta del laboratorio y sus graficas.
CARPETA_LABORATORIO = Path(__file__).resolve().parent
CARPETA_GRAFICAS = CARPETA_LABORATORIO / "graficas"

# SECCION 1. GENERACIÓN DE GUIAS INEXISTENTES

def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador para reproducir la medicion.

    Returns:
        Una lista con las guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes



# SECCION 2. FUNCIONES AUXILIARES


def es_primo(numero: int) -> bool:
    """Determina si un numero es primo.

    Args:
        numero: numero que se desea comprobar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 1

    return True


def siguiente_primo(numero: int) -> int:
    """Encuentra el primer numero primo mayor o igual al recibido.

    Args:
        numero: numero desde el cual comenzar la busqueda.

    Returns:
        El primer numero primo encontrado.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int]
) -> float:
    """Mide el tiempo promedio de una serie de busquedas.

    Args:
        estructura: lista enlazada o tabla hash que se va a evaluar.
        consultas: guias que se utilizaran en las busquedas.

    Returns:
        Tiempo promedio por busqueda en segundos.
    """
    inicio = time.perf_counter()

    for guia in consultas:
        estructura.buscar(guia)

    fin = time.perf_counter()

    tiempo_total = fin - inicio

    return tiempo_total / len(consultas)


def verificar_resultados(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
    estados: list[str]
) -> None:
    """Compara los resultados de ambas estructuras.

    Args:
        lista: lista enlazada construida.
        tabla: tabla hash construida.
        guias: guias existentes que se van a verificar.
        estados: estados correspondientes a las guias.
    """
    # Comprobar una muestra de hasta 100 guias existentes.
    cantidad = min(100, len(guias))

    for i in range(cantidad):
        resultado_lista = lista.buscar(guias[i])
        resultado_tabla = tabla.buscar(guias[i])

        assert resultado_lista == estados[i]
        assert resultado_tabla == estados[i]



# SECCION 3. EXPERIMENTO A: LISTA FRENTE A TABLA HASH

def experimento_a() -> None:
    """Compara el tiempo de busqueda de ambas estructuras.

    Evalua seis tamanos de entrada y genera la primera grafica.
    """
    tamanos = [100, 500, 1000, 5000, 20000, 50000]

    tiempos_lista = []
    tiempos_tabla = []
    tamanos_tabla = []

    print("\nEXPERIMENTO A: LISTA FRENTE A TABLA HASH")
    print("=" * 75)

    print(
        f"{'Guias (n)':<12}"
        f"{'Casillas (m)':<15}"
        f"{'Factor carga':<16}"
        f"{'Lista (s)':<16}"
        f"{'Tabla hash (s)':<16}"
    )

    # Evaluar cada cantidad de guias.
    for n in tamanos:

        # 1. Generar las guias existentes.
        azar = random.Random(42)

        guias = azar.sample(
            range(10**9, 10**10),
            n
        )

        # Asignar un estado a cada guia.
        estados = [
            ["en bodega", "en reparto", "entregado"][i % 3]
            for i in range(n)
        ]

        
        # 2. Construir ambas estructuras.
        lista = ListaEnlazada()

        # Elegir un numero primo cercano a n / 2.
        m = siguiente_primo(n // 2)

        tabla = TablaHash(m)

        # Insertar exactamente las mismas guias.
        for guia, estado in zip(guias, estados):
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # 3. Verificar que ambas estructuras respondan igual.
        verificar_resultados(lista, tabla, guias, estados)

        # 4. Generar 200 guias inexistentes.
        conjunto_existentes = set(guias)

        consultas = generar_guias_inexistentes(
            conjunto_existentes,
            200,
            semilla=7
        )

        # 5. Medir las busquedas de la lista enlazada.
        tiempo_lista = medir_busquedas(lista, consultas)


        # 6. Medir las busquedas de la tabla hash.
        tiempo_tabla = medir_busquedas(tabla, consultas)

        # Guardar los resultados para la grafica.
        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)
        tamanos_tabla.append(m)

        # Mostrar los resultados en la terminal.
        print(
            f"{n:<12}"
            f"{m:<15}"
            f"{tabla.factor_carga():<16.4f}"
            f"{tiempo_lista:<16.8f}"
            f"{tiempo_tabla:<16.8f}"
        )


    # 7. Generar la primera grafica.
    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanos,
        tiempos_lista,
        marker="o",
        label="Lista enlazada"
    )

    plt.plot(
        tamanos,
        tiempos_tabla,
        marker="s",
        label="Tabla hash"
    )

    plt.title("Tiempo de busqueda: lista enlazada vs tabla hash")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo promedio por busqueda (segundos)")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=300)
    plt.close()

    print("\nGrafica generada: graficas/lista_vs_tabla.png")



# SECCION 4. EXPERIMENTO B: EFECTO DEL FACTOR DE CARGA


def experimento_b() -> None:
    """Mide el tiempo de busqueda con distintos factores de carga.

    Mantiene fija la cantidad de guias y genera la segunda grafica.
    """
    n = 20000

    factores_objetivo = [0.5, 1, 4, 10]

    factores_reales = []
    tiempos_tabla = []

    print("\nEXPERIMENTO B: EFECTO DEL FACTOR DE CARGA")
    print("=" * 65)

    print(
        f"{'Guias (n)':<15}"
        f"{'Casillas (m)':<15}"
        f"{'Factor carga':<16}"
        f"{'Tiempo medio (s)':<18}"
    )


    # 1. Generar las mismas guias para todas las tablas.

    azar = random.Random(42)

    guias = azar.sample(
        range(10**9, 10**10),
        n
    )

    estados = [
        ["en bodega", "en reparto", "entregado"][i % 3]
        for i in range(n)
    ]

    # Construir una lista enlazada de referencia.
    lista = ListaEnlazada()

    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)

    # Generar las mismas 200 consultas inexistentes.
    conjunto_existentes = set(guias)

    consultas = generar_guias_inexistentes(
        conjunto_existentes,
        200,
        semilla=7
    )


    # 2. Construir y medir una tabla por cada factor objetivo.

    for alfa_objetivo in factores_objetivo:

        # Calcular la cantidad aproximada de casillas.
        m_objetivo = int(n / alfa_objetivo)

        # Utilizar el siguiente numero primo.
        m = siguiente_primo(m_objetivo)

        tabla = TablaHash(m)

        # Insertar las mismas guias en la nueva tabla.
        for guia, estado in zip(guias, estados):
            tabla.insertar(guia, estado)

        # Verificar una muestra de guias existentes.
        verificar_resultados(lista, tabla, guias, estados)

        # Medir las busquedas de guias inexistentes.
        tiempo_tabla = medir_busquedas(tabla, consultas)

        # Obtener el factor de carga real.
        alfa_real = tabla.factor_carga()

        factores_reales.append(alfa_real)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n:<15}"
            f"{m:<15}"
            f"{alfa_real:<16.4f}"
            f"{tiempo_tabla:<18.8f}"
        )


    # 3. Generar la segunda grafica.
    plt.figure(figsize=(10, 6))

    plt.plot(
        factores_reales,
        tiempos_tabla,
        marker="o",
        label="Tabla hash"
    )

    plt.title("Tiempo de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa)")
    plt.ylabel("Tiempo promedio por busqueda (segundos)")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=300)
    plt.close()

    print("\nGrafica generada: graficas/tiempo_vs_alfa.png")



# SECCION 5. EJECUCION DE LOS EXPERIMENTOS

if __name__ == "__main__":

    # Crear la carpeta de graficas dentro del laboratorio.
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    # Ejecutar el experimento A.
    experimento_a()

    # Ejecutar el experimento B.
    experimento_b()

    print("\nTodos los experimentos finalizaron correctamente.")
