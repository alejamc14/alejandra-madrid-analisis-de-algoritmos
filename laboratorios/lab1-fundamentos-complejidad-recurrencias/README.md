
# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
### **Nombre:** Alejandra Madrid Calderón


## Parte 1 — Analizar el algoritmo antes de comprar hardware
**Pregunta:** La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. ¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?

**Respuesta:** Antes de comprar un servidor, primero se debe garantizar un buen análisis del algoritmo implementado, ya que un problema de tiempo de ejecución no necesariamente se soluciona aumentando la capacidad del hardware. En este caso,  se utiliza el insertion sort que es capaz de procesar correctamente la lista ordenada, pero la cantidad de información ha aumentado durante los ocho años de funcionamiento del sistema y por eso este algoritmo que antes podía cumplir con las necesidades requeridas ahora tiene dificultades para procesar 1.200.000 de registros dentro de las de cuatro horas de tiempo requeridas, no es que no funcione, pero ya no cumple con la necesidad. 

Al duplicar la capacidad del servidor podría disminuirse el tiempo,  pero esto no cambia la forma en que el algoritmo ordena la lista cuando la cantidad de registros crece. Por ejemplo, esto mismo podría pasar en una base de datos universitaria con millones de registros de estudiantes, si se requiere consultar alguna información y el sistema se demora varios minutos cuando debería ser en pocos segundos entonces el algoritmo sería correcto pero no cumpliría la restricción de tiempo establecida para el sistema. 

## Parte 2 — Responsabilidad ambiental y ética de la implementación
**Pregunta:** Como responsable técnico de Tamiza, ¿qué responsabilidad ambiental y ética asume al decidir qué algoritmo de ordenamiento se ejecuta cada madrugada sobre los datos de 1.200.000 pacientes?

**Respuesta:** Es claro que como responsable técnico se asume una gran responsabilidad no solo para garantizar que el sistema funcione sino también en temas ambientales y éticos debido al impacto sobre los recursos tecnológicos y sobre las personas que son priorizadas o no según el sistema. 

En el aspecto ambiental, un proceso que se demora más consume mucho más recursos, lo que genera también un mayor consumo de energía y se vuelve una cifra significativa con el tiempo ya que son procesos que se repiten diariamente. Desde lo ético, la responsabilidad es aún mayor por tratarse de personas con condiciones de salud que exigen una atención prioritaria, por lo tanto si el sistema de ordenamiento falla o no se completa en el tiempo requerido el principal afectado por esta situación es el paciente, debido al posible retraso en su proceso de atención. Además la secretaría y el equipo encargado del sistema también tendrían que asumir consecuencias operativas y técnicas por no disponer de la lista completa.

## Parte 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

### 3.1 — Explicación
El peor caso ocurre cuando la lista viene en el orden contrario al que se necesita y por lo tanto debe hacer una mayor cantidad de comparaciones, el mejor caso es cuando la lista ya viene casi ordenada  y solo se aplica un mínimo de comparaciones, mientras que el caso promedio se da cuando viene en un orden al azar.

Para decidir si el algoritmo se puede pasar a producción se debe utilizar el peor caso, ya que este me permite conocer si el sistema podría cumplir con el máximo de tiempo definido de 4 horas en el caso menos favorable, debido a que esta implementación ejecuta el caso donde tiene que hacer la mayor cantidad de comparaciones, lo cual garantiza el límite máximo de  tiempo que tardaria el proceso con cualquier entrada distinta.
 
**Escenario A:** representa el caso promedio porque el orden viene aleatorio.

**Escenario B:** es el mejor caso,  ya que al tener el 98 % en orden casi no hará desplazamientos.

**Escenario C:** es el peor caso, ya que viene de menor a mayor y debe mover cada elemento hasta el principio.

### 3.2 — Demostración experimental

**Gráfica de comparaciones**

![parte3_comparaciones.png](./graficas/parte3_comparaciones.png)

**Gráfica de tiempo**

![parte3_tiempo.png](./graficas/parte3_tiempo.png)

Los resultados de las gráficas confirman la predicción realizada anteriormente, según el tiempo de ejecucion y el número de comparaciones, donde B es el mejor caso, C el peor caso y A es el caso intermedio.

## Parte 4 — Complejidad de merge sort e insertion sort: cálculo y validación

### 4.1 — Cálculo teórico

### Merge Sort

Merge Sort divide la lista en dos partes, ordena cada una recursivamente y luego combina las dos partes ordenadas.

La recurrencia es:

$$
T(n)=2T\left(\frac{n}{2}\right)+\Theta(n)
$$

Donde:

* $2$: se generan **2 subproblemas**.
* $n/2$: cada subproblema tiene la mitad de los elementos.
* $\Theta(n)$: combinar las dos mitades requiere recorrer sus elementos.

Por tanto:

$$
a=2,\qquad b=2,\qquad f(n)=\Theta(n)
$$

#### Método maestro

La forma general es:

$$
T(n)=aT\left(\frac{n}{b}\right)+f(n)
$$

Calculamos:

$$
n^{\log_b a}=n^{\log_2 2}
$$

$$
n^{\log_2 2}=n^1=n
$$

Comparamos con $f(n)$:

$$
f(n)=\Theta(n)
$$

Por lo tanto:

$$
f(n)=\Theta\left(n^{\log_b a}\right)
$$

Se cumple el **caso 2 del método maestro**, con $k=0$:

$$
f(n)=\Theta\left(n^{\log_b a}\log^0n\right)
$$

El resultado del caso 2 es:

$$
T(n)=\Theta\left(n^{\log_ba}\log^{0+1}n\right)
$$

Sustituyendo:

$$
T(n)=\Theta\left(n^1\log n\right)
$$

$$
T(n)=\Theta(n\log n)
$$

**Cota final:**

$$
\boxed{\Theta(n\log n)}
$$

---

### Insertion Sort

Para realizar el conteo se considera la siguiente implementación. Los comentarios indican cuántas veces puede ejecutarse cada línea en el **peor caso**:

```python
def insertion_sort(datos: list[int]) -> list[int]:
    resultado = datos.copy()       # 1 vez (costo lineal por la copia)

    for i in range(1, len(resultado)):  # n - 1 iteraciones
        clave = resultado[i]            # n - 1 veces
        j = i - 1                       # n - 1 veces

        while j >= 0 and resultado[j] > clave:  # Σ(i) + (n - 1)
            resultado[j + 1] = resultado[j]     # Σ(i)
            j -= 1                              # Σ(i)

        resultado[j + 1] = clave       # n - 1 veces

    return resultado                   # 1 vez
```

En el peor caso, la lista está ordenada de forma inversa. Para cada posición $i$, el `while` puede desplazarse $i$ veces.

Por tanto, el número total de ejecuciones del cuerpo del `while` es:

$$
1+2+3+\cdots+(n-1)
$$

Aplicando la fórmula de la suma:

$$
\sum_{i=1}^{n-1}i
=
\frac{n(n-1)}{2}
$$

Por lo tanto:

* La línea de desplazamiento se ejecuta $\frac{n(n-1)}{2}$ veces.
* La línea `j -= 1` se ejecuta $\frac{n(n-1)}{2}$ veces.
* La condición del `while` se comprueba una vez adicional por cada iteración del `for`:

$$
\frac{n(n-1)}{2}+(n-1)
$$

Los demás costos son lineales:

$$
T(n)=
c_1n+
c_2(n-1)+
c_3(n-1)+
c_4(n-1)+
c_5\left(\frac{n(n-1)}{2}+n-1\right)
$$

$$
+c_6\frac{n(n-1)}{2}
+c_7\frac{n(n-1)}{2}
+c_8(n-1)+c_9
$$

Los términos dominantes son cuadráticos:

$$
\frac{n(n-1)}{2}=\frac{n^2-n}{2}
$$

Por lo tanto:

$$
T(n)=\Theta(n^2)
$$

**Cota final del peor caso:**

$$
\boxed{\Theta(n^2)}
$$

---

### Tabla de complejidades

| Algoritmo          | Mejor caso        | Caso promedio     | Peor caso         |
| ------------------ | ----------------- | ----------------- | ----------------- |
| **Merge Sort**     | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n\log n)$ |
| **Insertion Sort** | $\Theta(n)$       | $\Theta(n^2)$     | $\Theta(n^2)$     |

