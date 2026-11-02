# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Alejandra Madrid Calderón · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `44982a4`

Muy buen trabajo: las estructuras funcionan y el informe está completo y ordenado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **91 / 100** |
| **Nota (0–5)** | **4.55** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Explica bien por qué hay colisiones aunque sobren casillas y usa el ejemplo de 10, 24 y 17 con m = 7.
- Explica que la tabla hash no conserva el orden y por eso no sirve para rangos.
- Recomienda una combinación (tabla hash + árbol equilibrado) y declara que la cifra de 5.000.000 es una aproximación.

**Lo que puede mejorar (y cómo corregirlo):**
- En el árbol degenerado da la altura, pero no cuenta cuántas comparaciones se hacen en total al insertar las 400.000 guías, y no las compara con el árbol equilibrado.
  → *Cómo corregirlo:* piense cuántas comparaciones cuesta insertar la guía número k cuando el árbol es una cadena y súmelas; luego haga lo mismo con una altura de unos 19 niveles.
- Sobre encadenamiento y direccionamiento abierto, las ventajas y costos quedan generales (no dice, por ejemplo, qué pasa con la tabla llena).
  → *Cómo corregirlo:* agregue qué le ocurre a cada método cuando α crece o se acerca a 1.
- En la pregunta 5 no da un tiempo para la tabla hash con 5.000.000 de envíos y no justifica la forma de la curva para elegir la extrapolación lineal.
  → *Cómo corregirlo:* apóyese en sus propios valores de la tabla (lista y tabla hash) para dar un número estimado para cada estructura y explique por qué esa forma de curva es la esperada.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y el Θ(1 + α) de la tabla.
- Nombra la distribución uniforme de las claves y explica que, si todas caen en una casilla, la búsqueda se vuelve Θ(n).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven el estado correcto, incluso para guías que no existen; `buscar` usa un ciclo `while`.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren la colisión con m = 7, el factor de carga 3/7 y 20 colecciones aleatorias; todas pasan.
- Hay docstrings con `Args` y `Returns`, type hints y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py` el bloque de importaciones aparece repetido dos veces.
  → *Cómo corregirlo:* deje una sola copia de las importaciones.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- Las dos gráficas existen, con título, ejes rotulados y leyenda; la primera cubre seis valores de n y la segunda cuatro valores de α.
- Los valores del informe coinciden con lo que se ve en las gráficas (lista cerca de 0.005 s con n = 50.000; tabla cerca de 1.7e-6 s con α ≈ 10).
- Calcula el factor de crecimiento de la lista (de 1.000 a 5.000 guías, unas 5.09 veces).

**Lo que puede mejorar (y cómo corregirlo):**
- No calcula el factor de crecimiento de la tabla hash entre dos valores de n; solo dice que "se mantuvo constante".
  → *Cómo corregirlo:* tome los mismos dos valores de n y divida el tiempo mayor entre el menor para la tabla, y compárelo con el de la lista.
- En el experimento B, α se multiplica por unas 20 y el tiempo por unas 3; el informe dice que es "coherente" sin explicar la relación con Θ(1 + α).
  → *Cómo corregirlo:* explique por qué el tiempo no crece 20 veces (hay una parte fija que no depende de α) y contraste el crecimiento con esa forma.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab3-estructuras-datos/` está en una ubicación válida y tiene todos los archivos pedidos.
- El README tiene su nombre, instrucciones de reproducción, enlaces al código en cada parte y las gráficas se ven.
- Hay cuatro commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y la medición corre completa y genera las dos gráficas.
