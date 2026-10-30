# Laboratorio 3 — Estructuras de datos
### **Nombre:** Alejandra Madrid Calderón

## Instrucciones para reproducir el experimento

### Requisitos

Para ejecutar los experimentos se requiere Python 3 y la biblioteca `matplotlib`.

El proyecto utiliza un entorno virtual para instalar y ejecutar las dependencias del laboratorio.

### Activar el entorno virtual
#### Instrucciones de ejecución por Sistema Operativo
Desde la carpeta raíz del repositorio:
1. En Windows (PowerShell / Command Prompt)

```powershell
# Activar el entorno virtual
.\venv\Scripts\activate

# Instalar dependencias (si no han sido instaladas previamente)
pip install -r requirements.txt

# Ejecutar las pruebas de verificación
python laboratorios/lab3-estructuras-datos/pruebas.py

# Ejecutar el experimento de medición de tiempos y generación de gráficas
python laboratorios/lab3-estructuras-datos/medicion.py 
```
2. En macOS y Linux (Bash / Zsh Terminal)
```powershell
# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar las pruebas de verificación
python laboratorios/lab3-estructuras-datos/pruebas.py

# Ejecutar el experimento de medición de tiempos y generación de gráficas
python laboratorios/lab3-estructuras-datos/medicion.py 
```



## Parte 1. Implementación de las estructuras

Se implementaron dos estructuras para almacenar y consultar las guías de envío:

- **Lista enlazada:** almacena los elementos mediante nodos conectados. La inserción se realiza al inicio en tiempo Θ(1), mientras que la búsqueda requiere recorrer los nodos hasta encontrar la guía o llegar al final, con complejidad Θ(n).
- **Tabla hash:** utiliza el método de división `guia % m` para determinar la casilla donde se almacena cada guía. Se implementó mediante encadenamiento, utilizando una lista enlazada en cada casilla para manejar las colisiones. Su búsqueda tiene un costo promedio Θ(1 + α), suponiendo una distribución uniforme de las claves.

La implementación se encuentra en [estructuras.py](estructuras.py) y las pruebas de funcionamiento en [pruebas.py](pruebas.py).

Las pruebas verifican búsquedas exitosas e infructuosas, colisiones, factor de carga y equivalencia de resultados entre ambas estructuras mediante 20 colecciones aleatorias.

## Parte 2. Experimentos de rendimiento

Los experimentos se desarrollaron en [medicion.py](medicion.py), utilizando `time.perf_counter()` para medir el tiempo promedio de búsqueda. En ambos experimentos se realizaron 200 consultas de guías inexistentes por estructura o configuración. La generación de datos y la construcción de las estructuras se realizaron antes del cronometraje.

### Experimento A. Lista enlazada vs. tabla hash

Se evaluaron seis tamaños de entrada. Para cada tamaño se seleccionó un número primo de casillas cercano a la mitad de la cantidad de guías, manteniendo un factor de carga aproximado de 2.

| Guías (n) | Casillas (m) | Factor de carga | Lista (s) | Tabla hash (s) |
|---:|---:|---:|---:|---:|
| 100 | 53 | 1.8868 | 0.00000406 | 0.00000024 |
| 500 | 251 | 1.9920 | 0.00002650 | 0.00000029 |
| 1.000 | 503 | 1.9881 | 0.00004287 | 0.00000030 |
| 5.000 | 2.503 | 1.9976 | 0.00021815 | 0.00000063 |
| 20.000 | 10.007 | 1.9986 | 0.00094466 | 0.00000118 |
| 50.000 | 25.013 | 1.9990 | 0.00524420 | 0.00000115 |

**Gráfica de resultados:**

![Tiempo de búsqueda: lista enlazada vs. tabla hash](graficas/lista_vs_tabla.png)

Los resultados muestran que el tiempo de búsqueda de la lista enlazada aumenta con el número de guías, mientras que la tabla hash conserva tiempos considerablemente menores.

### Experimento B. Efecto del factor de carga

Se mantuvo constante la cantidad de 20.000 guías y se modificó el número de casillas para evaluar cuatro factores de carga diferentes.

| Guías (n) | Casillas (m) | Factor de carga | Tiempo promedio (s) |
|---:|---:|---:|---:|
| 20.000 | 40.009 | 0.4999 | 0.00000056 |
| 20.000 | 20.011 | 0.9995 | 0.00000060 |
| 20.000 | 5.003 | 3.9976 | 0.00000104 |
| 20.000 | 2.003 | 9.9850 | 0.00000168 |

**Gráfica de resultados:**

![Tiempo de búsqueda según el factor de carga](graficas/tiempo_vs_alfa.png)

Se observa que el tiempo promedio de búsqueda aumenta a medida que crece el factor de carga, debido a que se incrementa la cantidad promedio de elementos almacenados en cada casilla.

## Parte 3. Análisis de resultados

### 1. Costo teórico
#### ¿Por qué la búsqueda en una lista enlazada es Θ(n) y en una tabla hash es Θ(1 + α) en promedio?

En una lista enlazada, cuando una guía no existe, es necesario recorrer todos los nodos para comprobar que no está almacenada. Por eso, el tiempo de búsqueda aumenta proporcionalmente al número de elementos y su complejidad es Θ(n).

En una tabla hash, la función hash permite acceder directamente a una casilla. Si las guías se distribuyen uniformemente, solo es necesario revisar los elementos de esa casilla. Por eso, su costo promedio es Θ(1 + α), donde α = n/m es el factor de carga.

Esta complejidad depende de una buena distribución de las claves. Si todas las guías terminan en una misma casilla, la búsqueda puede degradarse hasta Θ(n), porque sería necesario recorrer una lista enlazada con todos los elementos.

### 2. Lo medido contra lo esperado.
#### ¿Los resultados medidos coinciden con lo esperado teóricamente?

En el experimento A, al pasar de 1.000 a 5.000 guías, el tamaño de la entrada se multiplicó por 5 y el tiempo de búsqueda de la lista pasó de 0.00004287 a 0.00021815 segundos, aproximadamente 5.09 veces más. Esto evidencia un crecimiento cercano al comportamiento lineal Θ(n).

En cambio, la tabla hash mantuvo tiempos mucho menores. Aunque presentó pequeñas variaciones, el factor de carga permaneció cercano a 2, por lo que el tiempo promedio se mantuvo prácticamente constante en comparación con el crecimiento de la lista.

En el experimento B, al aumentar el factor de carga de aproximadamente 0.5 a 10, el tiempo pasó de 0.00000056 a 0.00000168 segundos. Esto representa un aumento de tres veces, coherente con la idea de que una mayor cantidad de elementos por casilla incrementa el trabajo de búsqueda.

Las pequeñas variaciones de los tiempos también pueden depender del entorno de ejecución y del costo de las operaciones medidas.

### 3. Explique las colisiones.
#### ¿Por qué existen colisiones incluso cuando m es mayor que n? ¿Qué ventajas y costos tiene el encadenamiento frente al direccionamiento abierto?

Las colisiones ocurren porque la función hash transforma una cantidad muy grande de posibles claves en un número limitado de casillas. Por esta razón, dos guías diferentes pueden obtener el mismo índice, incluso cuando hay más casillas que elementos.

Por ejemplo, con m = 7, las guías 10, 24 y 17 producen el mismo resultado:

- 10 % 7 = 3
- 24 % 7 = 3
- 17 % 7 = 3

El encadenamiento permite almacenar los elementos que colisionan en una lista enlazada dentro de la misma casilla. Su ventaja es que facilita la inserción y el manejo de colisiones sin buscar otra posición libre. Su costo es que requiere memoria adicional para los nodos y puede aumentar el tiempo de búsqueda cuando las listas crecen.

El direccionamiento abierto almacena todos los elementos directamente en la tabla y busca otras posiciones disponibles cuando ocurre una colisión. Puede aprovechar mejor la memoria al evitar listas enlazadas, pero necesita estrategias para encontrar posiciones libres y manejar las eliminaciones.

### 4. Tabla hash o árbol de búsqueda.
#### ¿Por qué una tabla hash no es adecuada para consultas por rango? ¿Qué ocurriría con un árbol binario de búsqueda?

Una tabla hash está diseñada para encontrar elementos mediante una clave exacta, pero no conserva el orden de las guías. Por eso, para consultar todas las guías entre X e Y sería necesario revisar los elementos almacenados, lo que resulta poco eficiente.

Un árbol binario de búsqueda sí organiza las claves de manera ordenada. Sin embargo, si se insertan 400.000 guías en orden creciente en un árbol sin balanceo, este puede degenerarse en una estructura similar a una lista enlazada. En ese caso, su altura sería de aproximadamente 399.999 aristas y una búsqueda podría necesitar hasta 400.000 comparaciones.

Si el árbol se mantiene equilibrado, su altura sería aproximadamente log₂(400.000), es decir, unos 19 niveles. Esto permite localizar el inicio del rango eficientemente y recorrer los k resultados, con un costo aproximado de Θ(log n + k).

### 5. Concepto para la jefa de operaciones.
#### ¿Qué estructura recomendaría para Rutas del Caribe y cuánto tardaría una búsqueda con 5 millones de guías?

Se recomienda utilizar una combinación de estructuras: una tabla hash para las consultas puntuales de guías y un árbol de búsqueda equilibrado para las consultas por rango.

Con base en el experimento A, la lista enlazada presentó un crecimiento cercano al lineal. Una extrapolación lineal de los datos medidos permite estimar que, con 5 millones de guías, una búsqueda infructuosa podría tardar alrededor de medio segundo. Esta es una aproximación y no una medición real.

Para la tabla hash, si se mantiene un factor de carga cercano a 2 y una distribución uniforme de las claves, se espera que el tiempo promedio de búsqueda continúe siendo prácticamente constante, incluso al aumentar la cantidad de guías. No obstante, el rendimiento real dependerá de la memoria disponible, las colisiones y la implementación.

Por lo tanto, la tabla hash es la alternativa más conveniente para las consultas puntuales, mientras que un árbol equilibrado permite atender eficientemente las consultas por rango.