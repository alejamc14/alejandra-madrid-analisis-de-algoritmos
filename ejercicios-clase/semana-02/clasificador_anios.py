"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese una lista de años separados por comas (ej. 2024, 1900, 2000): ")
        try:
            # Separamos por comas, limpiamos espacios y convertimos a enteros
            partes = entrada.split(",")
            anios = [int(parte.strip()) for parte in partes if parte.strip() != ""]
            
            if not anios:
                print("La lista no puede estar vacía. Intente de nuevo.")
                continue
                
            return anios
        except ValueError:
            print("Error: Asegúrese de ingresar únicamente números enteros separados por comas.")


def main() -> None:
    """Punto de entrada del script."""
    anios_usuario = leer_anios()
    
    # Filtramos usando comprensión de listas
    bisiestos = [anio for anio in anios_usuario if es_bisiesto(anio)]
    
    # Imprimimos el resumen requerido
    print("\n--- Resumen del Análisis ---")
    print(f"Total de años evaluados: {len(anios_usuario)}")
    print(f"Años bisiestos encontrados: {bisiestos}")
    print(f"Cantidad de años bisiestos: {len(bisiestos)}")


if __name__ == "__main__":
    main()
