# Alumno: Damián Jorge Portillo
# Trabajo Práctico 5 - Funciones en Python

import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones que calculan área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que devuelve una tupla con suma, resta, multiplicación y división
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero"
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    # 1
    
    # Enunciado - Actividad 1
    ej_1 = '''\n1) Crear una función llamada imprimir_hola_mundo que imprima por 
pantalla el mensaje: “Hola Mundo!”. 
Llamar a esta función desde el programa principal.\n'''
    print(ej_1)
    
    # Resolución - Actividad 1
    imprimir_hola_mundo()

    # Enunciado - Actividad 2
    ej_2 = '''\n2)  Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. \n'''
    print(ej_2)

    # Resolución - Actividad 2
    nombre = input("\nIngresá tu nombre: ")
    print(saludar_usuario(nombre))

    # Enunciado - Actividad 3
    ej_3 = '''\n3)  Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados.\n'''
    print(ej_3)
    
    # Resolución - Actividad 3
    nombre = input("\nNombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # Enunciado - Actividad 4
    ej_4 = '''\n4) Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.\n'''
    print(ej_4)

    # Resolución - Actividad 4
    radio = float(input("\nIngresá el radio de un círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # Enunciado - Actividad 5
    ej_5 = '''\n5) Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función. \n'''
    print(ej_5)

    # Resolución - Actividad 5
    segundos = int(input("\nIngresá una cantidad de segundos: "))
    print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

    # Enunciado - Actividad 6
    ej_6 = '''\n6) Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción. \n'''
    print(ej_6)

    # Resolución - Actividad 6
    numero = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # Enunciado - Actividad 7
    ej_7 = '''\n7) Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara. \n'''
    print(ej_7)

    # Resolución - Actividad 7
    a = float(input("\nPrimer número: "))
    b = float(input("Segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

    # Enunciado - Actividad 8
    ej_8 = '''\n8) Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales. \n'''
    print(ej_8)

    # Resolución - Actividad 8
    peso = float(input("\nIngresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")

    # Enunciado - Actividad 9
    ej_9 = '''\n9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. \n'''
    print(ej_9)

    # Resolución - Actividad 9
    celsius = float(input("\nTemperatura en grados Celsius: "))
    print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

    # Enunciado - Actividad 10
    ej_10 = '''\n10) .Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. \n'''
    print(ej_10)

    # Resolución - Actividad 10
    n1 = float(input("\nPrimer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    print(f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")
