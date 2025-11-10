"""
-----------------------------------------------------------------------------------------------------
Ejercicio 1: Primera Variable
Crear una variable llamada 'nombre' con tu nombre y otra 'edad' con tu edad.
Imprimir ambas variabes en una sola línea utilizando una f-string.

Conceptos:
- Variables son contenedores para almacenar datos
- Python es dinámicamente tipado (no necesitas declarar tipo)
- El operador = asigna valores
"""

print(".......................................................")
print("Ejercicio 1: Primera Variable / Dificultad : ⭐ Fácil / Tiempo: 5 minutos") 
print("...")

# Solución
nombre = "Carlos"
edad = 41
print(f"Me llamo {nombre} y tengo {edad} años")

print("...")
# Explicación:
# - Las comillas indican que es un string (texto)
# - Los números sin comillas son integers (enteros)
# - f"..." permite insertar variables dentro del tex


"""
-----------------------------------------------------------------------------------------------------
Ejercicio 2: Tipos de Datos
Crear 5 variables, una de cada tipo:
- str (string/texto)
- int (entero)
- float (decimal)
- bool (booleano)
- list (lista)

Imprimir cada una con su tipo usando type()
"""

print(".......................................................")
print("Ejercicio 2: Tipos de Datos / Dificultad : ⭐ Fácil / Tiempo: 10 minutos") 
print("...")

# Solución
texto = "Hola Python"       # str: cadena de texto
entero = 42                 # int: número entero
decimal = 3.14159           # float: número con decimales
booleano = True             # bool: verdadero/falso
lista = [1, 2, 3, 4, 5]     # list: colección de elementos

print(f"{texto} es tipo: {type(texto)}")
print(f"{entero} es tipo: {type(entero)}")
print(f"{decimal} es tipo: {type(decimal)}")
print(f"{booleano} es tipo: {type(booleano)}")
print(f"{lista} es tipo: {type(lista)}")

print("...")
# Explicación:
# type() retorna el tipo de dato de una variable
# Python tiene tipado dinámico: la variable se adapta al valor asignado

"""
-----------------------------------------------------------------------------------------------------
Ejercicio 3: Operaciones Matemáticas Básicas

Crear dos variables (num1 y num2) y realizar:
- Suma
- Resta
- Multiplicación
- División
- División entera
- Módulo (resto)
- Potencia
"""

print(".......................................................")
print("Ejercicio 3: Operaciones Matemáticas Básicas / Dificultad : ⭐ Fácil / Tiempo: 10 minutos") 
print("...")

# Solución
num1 = 10
num2 = 3

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")

print("...")
# Explicación:
# // devuelve solo la parte entera de la división
# % devuelve el resto (útil para saber si es par/impar)
# ** es la potencia (no ^)

"""
-----------------------------------------------------------------------------------------------------
Ejercicio 4: Conversión de Tipos

Convertir entre diferentes tipos de datos:
- String a int
- String a float
- Int a string
- Float a int
- Bool a int
"""

print(".......................................................")
print("Ejercicio 4: Conversión de Tipos / Dificultad : ⭐ Fácil / Tiempo: 10 minutos") 
print("...")

# Solución
texto_numero = "123"
texto_decimal = "45.67"
numero = 100
decimal = 3.14
verdadero = True

# Conversiones
a_entero = int(texto_numero)    # str a int
a_float = float(texto_decimal)   # str a float
a_string = str(numero)           # int a str
float_a_int = int(decimal)       # float a int
bool_a_int = int(verdadero)      # bool a int

print(f"'{texto_numero}' convertido a int: {a_entero}")
print(f"'{texto_decimal}' convertido a float: {a_float}")
print(f"'{numero}' convertido a string: {a_string}")
print(f"'{decimal}' convertido a int: {float_a_int}")
print(f"'{verdadero}' convertido a int: {bool_a_int}")

print("...")
# Explicación:
# int() trunca decimales (no redondea)
# str() convierte cualquier cosa a texto
# bool a int: True = 1, False = 0
# Si intentas int("texto") → ValueError

"""
-----------------------------------------------------------------------------------------------------
Ejercicio 5: Input del Usuario

Pedir al usuario:
- Su nombre
- Su edad
- Su altura (en metros)

Imprimir un mensaje personalizado con toda la info.
"""

print(".......................................................")
print("Ejercicio 5: Input del Usuario / Dificultad : ⭐ Fácil / Tiempo: 10 minutos")
print("...")

# Solución
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
altura = input("¿Cuál es tu altura en mertros? ")

print("\nResumen de tu información")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"\nHola {nombre}, tienes {edad} años y mides {altura}m")

print("...")
# Explicación:
# input() SIEMPRE retorna un string
# Debes convertir con int() o float() si necesitas números
# \n es un salto de línea

"""
-----------------------------------------------------------------------------------------------------
Ejercicio 6: Calculadora Simple

Crear una calculadora que:
1. Pida dos números al usuario
2. Muestre todas las operaciones básicas
3. Maneje división por cero
"""

print(".......................................................")
print("Ejercicio 6: Calculadora Simple / Dificultad : ⭐⭐ Medio / Tiempo: 15 minutos")
print("...")

# Solución
print("=== CALCULADORA SIMPLE ===")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# Manejo de división por cero
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print(f"{num1} / {num2} = Error: División por cero")
    print(f"{num1} // {num2} = Error: División por cero")
    print(f"{num1} % {num2} = Error: División por cero")

print("...")
# Explicación:
# float() permite decimales en la entrada
# if verifica condición antes de dividir
# != significa "diferente de"