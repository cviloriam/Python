# Utilidad de Medición de Tiempo en Python

Este repositorio contiene scripts de utilidad para proyectos en Python. La herramienta principal es `medir_tiempo.py`, un módulo simple para cronometrar la ejecución de bloques de código.

## 📂 Archivos del Repositorio

* **`medir_tiempo.py`**: El módulo principal. Contiene la función `medir_tiempo()` que actúa como un cronómetro.
* **`hola_mundo_v2.py`**: Un script de ejemplo que demuestra cómo importar y usar `medir_tiempo()`.

---

## ⚡ Características de `medir_tiempo`

La función `medir_tiempo()` es un cronómetro "stateful" (con estado) que facilita la medición del rendimiento:

* **Fácil de Usar**: Llama a la función una vez para iniciar el cronómetro y otra vez (con la misma clave) para detenerlo.
* **Múltiples Tareas**: Puede manejar múltiples cronómetros en paralelo usando diferentes `clave_tarea`.
* **Consciente de la Zona Horaria**: Muestra la hora local del servidor y la hora de Bogotá (`America/Bogota`) para un mejor contexto en los *logs*.
* **Reporte Claro**: Calcula la duración total y la presenta en un formato legible (minutos y segundos).

---

## 🛠️ Requisitos e Instalación

1.  **Python**: Se requiere **Python 3.9** o superior (debido al uso del módulo `zoneinfo`).
2.  **Dependencia `tzdata`**: El módulo `zoneinfo` necesita la base de datos de zonas horarias. Debes instalarla usando pip:

    ```bash
    pip install tzdata
    ```

3.  **Módulo Local**: Asegúrate de que el archivo `medir_tiempo.py` esté en la misma carpeta que el script que lo va a importar.

---

## 🚀 Cómo Usar

Simplemente importa la función y "envuelve" el bloque de código que deseas medir con las llamadas de inicio y fin.

```python
from medir_tiempo import medir_tiempo
import time

print("Iniciando un proceso largo...")

# 1. Inicia el cronómetro para "Proceso_Largo"
medir_tiempo("Proceso_Largo")

# --- Tu código a medir ---
time.sleep(1.5) # Simulación de una tarea
print("...trabajo intermedio...")
time.sleep(1.0) # Más simulación
# --- Fin de tu código ---

# 2. Detiene el cronómetro para "Proceso_Largo"
medir_tiempo("Proceso_Largo")
