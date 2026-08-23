"""
    Código anterior: 
    def CalcularPromedio(Lista):
        s=0
        for x in Lista:
        s=s+x
        return s/len(Lista)
    
    l=[1,2,3,4,5]
    print(CalcularPromedio(l))
"""


def calcular_promedio(Lista_numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Una lista que contiene números enteros o decimales.

    Returns:
        float: El promedio obtenido de la suma de los elementos dividida entre su cantidad.
    """
    suma = 0
    for x in Lista_numeros:
        suma += x
    return suma / len(Lista_numeros)



def main() -> None:
    # Lógica principal del script protegida
    lista_ejemplo = [1, 2, 3, 4, 5]
    resultado = calcular_promedio(lista_ejemplo)
    print(resultado)


if __name__ == "__main__":
    main()