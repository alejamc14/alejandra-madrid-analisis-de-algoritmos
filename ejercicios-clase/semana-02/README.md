# Configuración del Entorno Virtual del Proyecto

Este proyecto utiliza un entorno virtual aislado para gestionar sus dependencias de forma limpia y reproducible.

## Instrucciones para gestionar el entorno:

1. **Creación del entorno virtual (desde la raíz):**
   ```bash
   py -m venv venv
   ```
2. **Activación del entorno en Windows:**
   ```bash
   .\venv\Scripts\activate
   ```
3. **Reproducción y réplica de librerías:**
   Cualquier otra persona puede instalar las dependencias exactas usando el archivo de configuración con:
   ```bash
   pip install -r requirements.txt
   ```
