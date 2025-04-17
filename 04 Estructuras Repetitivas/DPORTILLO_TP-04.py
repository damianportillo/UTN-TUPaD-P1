print('\nAlumno: Damián Jorge Portillo.\n')
print('Práctico 4: Estructuras repetitivas. \n')
print('Actividades.\n')

# Enunciado - Actividad 1
ej_1 = '''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.\n'''
print(ej_1)

# Resolución - Actividad 1
for i in range(101):
    print(i)

# Enunciado - Actividad 2
ej_2 = '''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. \n'''
print(ej_2)

# Resolución - Actividad 2
# solicito ingresar un numero
entrada = input("Ingresa un número: ")
# valido que sea un entero
try:
    num = int(entrada)
    # abs() es para ignorar el signo si es negativo.
    # str() es para convertir en string, cosa de poder usar len().
    # len() cuenta la longitud de una cadena.
    count = len(str(abs(num)))

    print(f"El número ingresado contiene {count} dígitos")
except ValueError:
    print("El número ingresado no es un entero.")


# Enunciado - Actividad 3
ej_3 = '''3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario,
excluyendo esos dos valores. \n'''
print(ej_3)

# Resolución - Actividad 3
# Pedir los dos valores al usuario
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
# Asegurarse de que el rango esté bien ordenado
menor = min(inicio, fin)
mayor = max(inicio, fin)
# Calcular la suma excluyendo los extremos
suma = 0
for numero in range(menor + 1, mayor):
    suma += numero
# Mostrar el resultado
print(f"La suma de los números entre {menor} y {mayor} (excluyéndolos) es: {suma}. \n")

# Enunciado - Actividad 4
ej_4 = '''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.\n'''
print(ej_4)

# Resolución - Actividad 4
# Inicializamos la variable para almacenar la suma total
suma_total = 0

# Bucle infinito hasta que el usuario ingrese 0
while True:
    # Solicitamos al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero (0 para terminar): "))

    # Si el número es 0, salimos del bucle
    if numero == 0:
        break

    # Sumamos el número ingresado al total
    suma_total += numero

# Mostramos la suma acumulada al final
print(f"La suma total de los números ingresados es: {suma_total}")


# Enunciado - Actividad 5
ej_5 = '''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. \n'''
print(ej_5)

# Resolución - Actividad 5
import random  # Importamos la librería para generar el número aleatorio

# Generamos un número secreto entre 0 y 9
numero_secreto = random.randint(0, 9)

# Contador de intentos
intentos = 0

# Inicia el juego
while True:
    try:
        # Solicitamos la entrada del usuario
        entrada = input("Adivina el número (entre 0 y 9): ")
        adivinanza = int(entrada)  # Intentamos convertir a entero

        # Verificamos que esté dentro del rango permitido
        if adivinanza < 0 or adivinanza > 9:
            print("Por favor, ingresa un número entre 0 y 9.")
            continue  # Volver al inicio del bucle sin contar como intento

        # Si es válido, incrementamos el contador
        intentos += 1

        # Comprobamos si adivinó
        if adivinanza == numero_secreto:
            print(f"¡Correcto! El número era {numero_secreto}.")
            break  # Salimos del bucle
        else:
            print("Incorrecto, intenta de nuevo.")

    except ValueError:
        # Si no se puede convertir a entero, mostramos un mensaje
        print("Entrada inválida. Debes ingresar un número entero entre 0 y 9.")

# Mostramos cuántos intentos fueron necesarios
print(f"Acertaste en {intentos} intento(s).")

# Enunciado - Actividad 6
ej_6 = '''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, 
en orden decreciente. \n'''
print(ej_6)

# Resolución - Actividad 6
# Recorremos los números del 100 al 0, bajando de 2 en 2
for numero in range(100, -1, -2):
    print(numero)

# Enunciado - Actividad 7
ej_7 = '''7) Crea un programa que calcule la suma de todos los números
comprendidos entre 0 y un número entero positivo indicado por el usuario. \n'''
print(ej_7)

# Resolución - Actividad 7
# Pedimos al usuario un número entero positivo
while True:
    try:
        limite = int(input("Ingrese un número entero positivo: "))
        if limite < 0:
            print("Debe ser un número positivo. Inténtalo de nuevo.")
        else:
            break  # Salimos del bucle si el número es válido
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entero.")

# Inicializamos la variable para acumular la suma
suma_total = 0

# Sumamos todos los números desde 0 hasta el número ingresado (inclusive)
for numero in range(0, limite + 1):
    suma_total += numero

# Mostramos el resultado
print(f"La suma de los números entre 0 y {limite} es: {suma_total}")


# Enunciado - Actividad 8
ej_8 = '''8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
Luego, el programa debe indicar cuántos de esos números son pares, cuántos son impares,
cuántos son negativos y cuántos son positivos.
(Nota: para probar el programa puedes usar una cantidad menor, 
pero debe estar preparado para procesar 100 números con un solo cambio). \n'''
print(ej_8)

# Resolución - Actividad 8
# Cantidad de números a ingresar (puedes cambiar esto fácilmente)
cantidad = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Recorremos la cantidad deseada de números
for i in range(1, cantidad + 1):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i}: "))
            break  # Salir del while si la entrada es válida
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    # Clasificación par/impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Clasificación positivo/negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # El 0 no se cuenta como positivo ni negativo, pero sí puede ser par

# Mostrar resultados
print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos} \n")


# Enunciado - Actividad 9
ej_9 = '''9) Elabora un programa que permita al usuario ingresar 100 números enteros,
y luego calcule la media (promedio) de esos valores.
(Nota: puedes probar el programa con una cantidad menor,
pero debe poder procesar 100 números cambiando solo un valor). \n'''
print(ej_9)

# Resolución - Actividad 9
# Cantidad de números que el usuario debe ingresar
cantidad = 100

# Lista para almacenar los números ingresados
numeros = []

# Pedimos los números al usuario
for i in range(1, cantidad + 1):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i}: "))
            numeros.append(numero)
            break  # Salimos del while si la entrada fue válida
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número entero.")

# Calculamos la media
suma_total = sum(numeros)
media = suma_total / cantidad

# Mostramos el resultado
print(f"\n La media de los {cantidad} números ingresados es: {media}. \n")


# Enunciado - Actividad 10
ej_10 = '''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. \n'''
print(ej_10)

# Resolución - Actividad 10
# Pedimos al usuario que ingrese un número
numero = input("Ingresa un número entero: ")

# Contamos la cantidad de dígitos en el número comenzando desde 0
cantidad_digitos = len(numero) - 1

# Usamos un for para imprimir los dígitos en orden inverso
# Desde el último dígito hasta el primero
numero_invertido = ""
for i in range(cantidad_digitos, -1, -1):  
    numero_invertido += numero[i]

# Mostramos el número invertido
print(f"El número invertido es: {numero_invertido}")
