"""
Módulo: 
    cv02_medir_tiempo.py
Descripción:
    Una utilidad de script simple para medir el tiempo de ejecución de tareas.
    Proporciona una función stateful (con estado) `medir_tiempo()` que actúa
    como un cronómetro. La primera vez que se llama con una clave de tarea,
    registra el inicio. La segunda vez con la misma clave, registra el fin,
    calcula la duración e imprime un informe.
    Este módulo está configurado para mostrar siempre la hora local del servidor
    y la hora de Bogotá (America/Bogota).
Dependencias:
    - python >= 3.9 (por el módulo 'zoneinfo')
    - tzdata (requerido por zoneinfo, instalar con: pip install tzdata en una consola power de windows)
Autor: 
    cviloriam
Fecha:
    2025-11-05
Versión:
    1.0.0
Repositorio: 
    https://github.com/cviloriam/Python
"""

# ============================================
# IMPORTACIONES
# ============================================
import datetime
from zoneinfo import ZoneInfo  # Para manejar zonas horarias (requiere Python 3.9+)

# ============================================
# CONSTANTES Y VARIABLES GLOBALES
# ============================================
# Almacén global para guardar los tiempos de inicio de las tareas.
# Es un diccionario donde:
#   - La clave (str) es el nombre de la tarea (clave_tarea)
#   - El valor (datetime) es el timestamp "aware" de cuándo se inició.
tiempo_inicio_global = {}

# Se define la zona horaria de Bogotá como una constante global.
# Esto es más eficiente que crear el objeto ZoneInfo cada vez que se llama a la función.
# Requiere que el paquete 'tzdata' esté instalado.
TZ_BOGOTA = ZoneInfo("America/Bogota")

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================
def medir_tiempo(clave_tarea="Tarea Principal"):
    """
    Inicia o detiene un cronómetro para una tarea específica.

    Esta función es "stateful". Depende de la variable global `tiempo_inicio_global`
    para saber si una tarea ya ha sido iniciada.

    - 1ra LLAMADA (con una clave_tarea): Inicia el cronómetro. Registra la hora
      de inicio en el diccionario global e imprime un mensaje [INICIO].
    - 2da LLAMADA (con la misma clave_tarea): Detiene el cronómetro. Calcula
      la duración, imprime un informe [FIN] y elimina la clave del diccionario
      para permitir que la tarea se vuelva a medir.

    :param clave_tarea: Un nombre (string) único para la tarea que se está
                        midiendo. Las llamadas de inicio y fin deben usar
                        exactamente la misma clave.
    :type clave_tarea: str, opcional
    :return: None. La función imprime su salida directamente en la consola.
    """
    
    # Se usa 'global' para indicar que vamos a MODIFICAR la variable
    # definida fuera del ámbito (scope) de esta función.
    global tiempo_inicio_global

   # --- Captura de Timestamps ---
    
    # 1. Hora de Bogotá: Es "timezone-aware" (consciente de la zona horaria).
    #    Se usará para todos los cálculos de duración, ya que es robusto.
    ahora_bogota = datetime.datetime.now(TZ_BOGOTA)
    
    # 2. Hora Local del Servidor: Es "timezone-naive" (ingenua).
    #    No sabe su propia zona horaria. Se usará solo para fines de visualización.
    ahora_local = datetime.datetime.now()
    
    # --- Lógica de la Función ---

    if clave_tarea not in tiempo_inicio_global:
        # --- LÓGICA DE INICIO ---
        # Si la clave no está en el diccionario, es la primera llamada.
        
        # Guardamos el timestamp de Bogotá (aware) para el cálculo futuro.
        tiempo_inicio_global[clave_tarea] = ahora_bogota 
        
       # Formatear ambas horas para una impresión limpia
        # %Y=Año, %m=Mes, %d=Día, %H=Hora(24h), %M=Min, %S=Seg
        hora_local_fmt = ahora_local.strftime("%Y-%m-%d %H:%M:%S")
        # %Z=Nombre de Zona (ej. COT), %z=Desfase UTC (ej. -0500)
        hora_bogota_fmt = ahora_bogota.strftime("%Y-%m-%d %H:%M:%S UTC %Z")

        # Imprimir el informe de INICIO
        print("\n" + "-" * 50) # <--- Hice la línea más ancha
        print(f"🚀 Tarea: '{clave_tarea}'")
        print(f"   [INICIO] Hora Servidor (Local) : {hora_local_fmt} / Hora Bogotá (COT) : {hora_bogota_fmt}")
        print("-" * 50 + "\n")

    else:
        # --- LÓGICA DE FINALIZACIÓN Y CÁLCULO ---
        # Si la clave SÍ está, es la segunda llamada (la de finalización).
        
       # 1. Recuperar y ELIMINAR la hora de inicio del diccionario.
        #    Usar .pop() es clave: obtiene el valor y limpia la entrada,
        #    dejando todo listo para volver a medir la misma tarea si es necesario.
        inicio = tiempo_inicio_global.pop(clave_tarea)
        
        # 2. Calcular la duración.
        #    Esto funciona sin problemas porque 'ahora_bogota' e 'inicio'
        #    son ambos objetos datetime "aware" de la misma zona horaria.
        duracion = ahora_bogota - inicio
        
        # 3. Convertir la duración a un formato legible
        segundos_totales = duracion.total_seconds()
        minutos_enteros = int(segundos_totales // 60)
        segundos_decimales = segundos_totales % 60

        # 4. Formatear las horas de finalización para la impresión
        hora_local_fmt = ahora_local.strftime("%Y-%m-%d %H:%M:%S")
        hora_bogota_fmt = ahora_bogota.strftime("%Y-%m-%d %H:%M:%S UTC %Z")

        # 5. Imprimir el informe de FIN
        print("\n" + "-" * 50)
        print(f"✅ Tarea: '{clave_tarea}'")
        print(f"   [FIN] Hora Servidor (Local) : {hora_local_fmt} / Hora Bogotá (COT) : {hora_bogota_fmt}")
        print(f"   Tiempo transcurrido: {minutos_enteros} minutos y {segundos_decimales:.3f} segundos.")
        print("-" * 50 + "\n")