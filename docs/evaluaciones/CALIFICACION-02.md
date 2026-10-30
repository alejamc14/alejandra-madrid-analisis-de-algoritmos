# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Alejandra Madrid Calderón · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `741f9c6`

Muy buen trabajo: el código funciona, la gráfica es clara y el análisis se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Indica desde qué tamaño gana divide y vencerás (n = 50) y explica por qué en tamaños muy pequeños la fuerza bruta es más rápida.
- Compara con hallar el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia es `T(n) = 2T(n/2) + Θ(1)` y concluye que dividir no aporta ventaja.
- Recomienda divide y vencerás y estima el tiempo con 1.000.000 de registros, declarándolo como estimación.

**Lo que puede mejorar:**
- En n = 50 la diferencia entre los dos algoritmos es muy pequeña; conviene decir que ahí están casi empatados y que la ventaja clara se ve desde n = 100 o más.
- La estimación parte de un solo tamaño (4.000). Sería más sólido mencionar que el resultado real puede variar (memoria, equipo).

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` y la resuelve con el método maestro verificando que se cumple el caso 2.
- Justifica que la fuerza bruta es `Θ(n²)` con la suma de n(n+1)/2 pares.

**Lo que puede mejorar:**
- Aclare que las dos mitades son de tamaño "aproximadamente" n/2 porque n puede ser impar (lo menciona, pero sin explicar el efecto).

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista de entrada.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Hay *type hints* y *docstrings* en las funciones de `subarreglo.py`.
- `pruebas.py` cubre todos los casos pedidos y 30 listas aleatorias con semilla fija.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre funciones en `pruebas.py` y `medicion.py`.
- Los *docstrings* de `medicion.py` y `pruebas.py` son de una línea, sin las secciones `Args` y `Returns` del estilo Google.
- El caso "cruzado" solo prueba `suma_cruzada`; también convenía probarlo con `subarreglo_maximo`.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados, leyenda y 7 tamaños.
- Calcula el factor al duplicar n (de 2000 a 4000): 3.15 para fuerza bruta y 2.06 para divide y vencerás, y los contrasta con 4 y 2.18. Los valores coinciden con lo que se lee en la gráfica.

**Lo que puede mejorar:**
- Decir que divide y vencerás "se mantiene prácticamente plana" es una exageración: sí crece, solo que queda pegada al eje. Una tabla con los tiempos medidos mostraría mejor los valores pequeños.
- Los valores de n = 10 y n = 50 que cita no se pueden leer en la gráfica; incluya una tabla con los tiempos medidos.
- El factor 3.15 queda algo lejos de 4; faltó explicar mejor esa diferencia (ruido, un solo par de tamaños).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida, con todos los archivos pedidos.
- El informe sigue el orden pedido, enlaza el código en cada parte, muestra la gráfica y tiene instrucciones de reproducción.
- Hay varios commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden y `medicion.py` corre en pocos segundos y genera la gráfica.

## Para el próximo laboratorio
- Deje dos líneas en blanco entre funciones en todos sus archivos antes de subir.
- Escriba los *docstrings* con `Args` y `Returns` en todas las funciones, también las de medición.
- Agregue una tabla con los tiempos medidos para apoyar lo que afirma en el análisis.
- Pruebe cada función también con el caso especial (por ejemplo, el cruzado) llamando a la función principal.
