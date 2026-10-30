
"""Pruebas de funcionamiento para la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash



# PRUEBA 1. FUNCIONAMIENTO DE LA LISTA ENLAZADA

lista = ListaEnlazada()

# Insertar algunas guias con sus respectivos estados.
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")
lista.insertar(1000000017, "entregado")

# Verificar que las guias existentes devuelvan su estado.
assert lista.buscar(1000000010) == "en bodega"
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000017) == "entregado"

# Verificar que una guia inexistente devuelva None.
assert lista.buscar(9999999999) is None

# Verificar que el tamano de la lista sea correcto.
assert lista.tamano == 3



# PRUEBA 2. FUNCIONAMIENTO DE LA TABLA HASH

# Crear una tabla hash con siete casillas.
tabla = TablaHash(7)

# Insertar las mismas guias y estados utilizados en la lista.
tabla.insertar(1000000010, "en bodega")
tabla.insertar(1000000024, "en reparto")
tabla.insertar(1000000017, "entregado")

# Verificar que las guias existentes devuelvan su estado.
assert tabla.buscar(1000000010) == "en bodega"
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000017) == "entregado"

# Verificar que una guia inexistente devuelva None.
assert tabla.buscar(9999999999) is None

# Verificar la cantidad total de guias almacenadas.
assert tabla.tamano == 3



# PRUEBA 3. COLISIONES Y FACTOR DE CARGA

# Crear una nueva tabla hash con siete casillas.
tabla_colisiones = TablaHash(7)

# Insertar tres guias que generan una colision.
# Las tres producen el indice 3 al aplicar el metodo de division.
for guia in (10, 24, 17):
    tabla_colisiones.insertar(guia, "en bodega")

# Verificar que las tres guias se asignen a la misma casilla.
assert tabla_colisiones.hash(10) == 3
assert tabla_colisiones.hash(24) == 3
assert tabla_colisiones.hash(17) == 3

# Verificar que las tres guias puedan buscarse correctamente.
assert tabla_colisiones.buscar(10) == "en bodega"
assert tabla_colisiones.buscar(24) == "en bodega"
assert tabla_colisiones.buscar(17) == "en bodega"

# Verificar que la lista enlazada de la casilla 3 tenga tres nodos.
assert tabla_colisiones.casillas[3].tamano == 3

# Verificar que la tabla tenga tres guias en total.
assert tabla_colisiones.tamano == 3

# Verificar el factor de carga: cantidad de guias / casillas.
assert tabla_colisiones.factor_carga() == 3 / 7



# PRUEBA 4. COMPARACION CON COLECCIONES ALEATORIAS

# Crear un generador aleatorio con semilla fija.
azar = random.Random(2026)

# Ejecutar veinte colecciones aleatorias.
for numero_prueba in range(20):

    # Generar una cantidad aleatoria de guias diferentes.
    cantidad = azar.randint(1, 100)

    guias = azar.sample(
        range(10**9, 10**10),
        cantidad
    )

    # Crear las dos estructuras que se van a comparar.
    lista_aleatoria = ListaEnlazada()
    tabla_aleatoria = TablaHash(127)

    # Insertar las mismas guias en ambas estructuras.
    for guia in guias:

        # Seleccionar aleatoriamente un estado para cada guia.
        estado = azar.choice([
            "en bodega",
            "en reparto",
            "entregado"
        ])

        lista_aleatoria.insertar(guia, estado)
        tabla_aleatoria.insertar(guia, estado)


    # Comprobar las busquedas de todas las guias existentes.
  
    for guia in guias:

        resultado_lista = lista_aleatoria.buscar(guia)
        resultado_tabla = tabla_aleatoria.buscar(guia)

        # Ambas estructuras deben devolver exactamente el mismo estado.
        assert resultado_lista == resultado_tabla


    # Generar veinte guias que no existan en la coleccion.
    inexistentes = []

    while len(inexistentes) < 20:

        guia = azar.randint(10**9, 10**10 - 1)

        # Evitar que las guias generadas pertenezcan a la coleccion.
        if guia not in guias:
            inexistentes.append(guia)

    # Comprobar que ambas estructuras respondan None.
    for guia in inexistentes:

        resultado_lista = lista_aleatoria.buscar(guia)
        resultado_tabla = tabla_aleatoria.buscar(guia)

        assert resultado_lista == resultado_tabla
        assert resultado_lista is None



# FINALIZACION DE LAS PRUEBAS
print("Todas las pruebas se ejecutaron correctamente.")
