# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Alejandra Madrid Calderón · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `eb733a8`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **71 / 100** |
| **Nota (0–5)** | **3.55** |

## 1. Corrección conceptual (14 / 25)
**Lo que hizo bien:**
- Explica que el algoritmo sí ordena bien, pero ya no cabe en las cuatro horas.
- Aclara que duplicar el servidor no cambia la forma en que el algoritmo crece con más registros.
- Reconoce que el paciente es el principal afectado si la lista no se completa.

**Lo que puede mejorar:**
- El segundo ejemplo (base de datos universitaria) no dice cuántos datos hay ni qué tiempo máximo se incumple.
- En la Parte 2 falta un segundo perjuicio concreto a una persona, con quién asume su costo.
- No explica cuánta energía se gasta ni por qué se acumula al repetirse cada madrugada durante años.
- Falta discutir que el orden de la lista decide a quién se llama primero y qué obligación extra impone eso sobre la corrección.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Escribe la predicción antes del experimento y la deja en el informe.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando el caso 2.
- Cuenta línea a línea el insertion sort y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- Al definir peor, mejor y caso promedio, falta decir sobre qué conjunto de entradas y con qué tamaño fijo se toma el máximo, el mínimo o el promedio.
- El código que usó para el conteo línea a línea no es el mismo que entregó (la versión del informe no cuenta comparaciones y compara al revés).

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, sin alterar la lista recibida y con conteo de comparaciones correcto. No usan `sorted()` ni `sort()`.
- Los tres generadores dan listas del tamaño pedido, sin repetidos y con semilla.

**Lo que puede mejorar:**
- Varias funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen todas las anotaciones de tipos, y `medir_escenario` no declara lo que devuelve.
- Falta una línea en blanco en `algoritmos.py`.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda.
- Identifica B como mejor caso, C como peor y A como intermedio, y la gráfica lo respalda.
- El concepto técnico recomienda merge sort, usa sus mediciones (6400 registros), extrapola a 1.200.000 declarándolo estimación y responde a la propuesta del servidor (unas 4,29 horas aun con el doble de velocidad). También menciona la memoria extra.

**Lo que puede mejorar:**
- El análisis de la Parte 3.2 no cita cifras concretas de sus mediciones ni explica con detalle cómo se compara con la predicción.
- En 4.2 describa mejor lo que hace cada curva y por qué cambia (por ejemplo, cuántas veces crece el tiempo al duplicar el tamaño).

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Carpeta del laboratorio en una ubicación válida, con todos los archivos y gráficas pedidos, que se ven en el informe.
- Cinco commits del laboratorio, con mensajes claros.

**Lo que puede mejorar:**
- El informe no enlaza el código de la Parte 3, ni el de la Parte 4, ni `algoritmos.py` y `datos.py`.
- Las instrucciones de reproducción solo sirven en Windows y mezclan comandos en un mismo bloque; los programas solo funcionan si se ejecutan desde la raíz del repositorio y eso no se explica claramente.

## ¿El código funciona?
Sí. Los programas corren sin errores, ordenan bien los tres escenarios y generan las tres gráficas cuando se ejecutan desde la raíz del repositorio.

## Para el próximo laboratorio
- Enlace en el informe cada archivo `.py` con su parte.
- Respalde las respuestas con números concretos (cantidad de datos, tiempos, energía) y con todos los puntos que pide cada pregunta.
- Use en el cálculo teórico el mismo código que entrega.
- Agregue anotaciones de tipos a todas las funciones.
- Explique cómo ejecutar los programas en cualquier sistema operativo.
