
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

