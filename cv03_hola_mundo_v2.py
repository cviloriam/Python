"""
Módulo: 
    hola_mundo_v2.py
Descripción: 
    Script de demostración que imprime un saludo "Hola, Mundo!"
    y utiliza el módulo 'medir_tiempo' para cronometrar
    cuánto tarda la ejecución, incluyendo una pausa simulada.
Autor: 
    cviloriam
Fecha: 
    2025-11-05
Versión: 
    2.0.0
Repositorio: 
    https://github.com/cviloriam/Python
Dependencias:
    - medir_tiempo.py (debe estar en la misma carpeta o en el PYTHONPATH)
"""

# ============================================
# IMPORTACIONES
# ============================================
# (Todas las importaciones deben ir aquí, al inicio del script)
from cv02_medir_tiempo import medir_tiempo
import time

# ============================================
# PROGRAMA PRINCIPAL
# ============================================
# La función print() muestra texto en la consola/terminal
# Sintaxis: print(objeto, sep=' ', end='\n', file=sys.stdout, flush=False)

print("\nInicio...(V)")

# 1. Inicia el cronómetro para la tarea "Saludo Hola Mundo"
medir_tiempo("Saludo Hola Mundo")

# 2. Tarea principal: Imprimir el saludo
print("Hola, Mundo 2.0!")
print("Con delay adicional para demostrar el cronómetro de 1.5 segundos...")

# 3. Simular trabajo adicional (ej. procesamiento, espera de red)
time.sleep(1.5)

# 4. Detiene el cronómetro para la tarea "Saludo Hola Mundo"
medir_tiempo("Saludo Hola Mundo")

print("(V)...Fin\n")

# Salida esperada:
# Hola, Mundo!
# (Y los bloques de INICIO/FIN de medir_tiempo)

# ============================================
# NOTAS ADICIONALES
# ============================================
# - Este es el clásico programa "Hello, World!" en español.
# - Ahora también demuestra el uso de un módulo de cronometraje.