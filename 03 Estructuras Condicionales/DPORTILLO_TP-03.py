print('\nAlumno: Damián Jorge Portillo.\n')
print('Práctico 3: Estructuras condicionales. \n')
print('Actividades.\n')

# Enunciado - Actividad 1
ej_1 = '''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.\n'''
print(ej_1)

# Resolución - Actividad 1
# Solicito ingresar edad
edad = int(input("Ingresa tu edad: "))
# Evalúo su edad
if edad > 18:
    print(f"“Es mayor de edad”.\n")


# Enunciado - Actividad 2
ej_2 = '''2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. \n'''
print(ej_2)

# Resolución - Actividad 2
# Solicito ingresar nota
nota = float(input("Ingresa tu nota: "))
# Evalúo nota
if nota >= 6:
   print(f"“Aprobado”.\n") 
else:
   print(f"“Desaprobado”.\n")


# Enunciado - Actividad 3
ej_3 = '''3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
imprimir en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. \n'''
print(ej_3)

# Resolución - Actividad 3
# Solicito igreso de datos
numero = int(input("Ingrese números pares: "))
# Evalúo número ingresado que sea par.
if numero % 2 == 0:
   print(f"“Ha ingresado un número par”.\n") 
else:
   print(f"“Por favor, ingrese un número par”.\n")



# Enunciado - Actividad 4
ej_4 = '''4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
                                ● Niño/a: menor de 12 años.
                                ● Adolescente: mayor o igual que 12 años y menor que 18 años.
                                ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
                                ● Adulto/a: mayor o igual que 30 años. \n'''
print(ej_4)

# Resolución - Actividad 4
# Solicito ingresar edad
edad = int(input("Ingresa tu edad: "))
# Evalúo su edad
if edad < 12:
    print(f"Niño/a: menor de 12 años. \n")
elif edad >= 12 and edad < 18:
    print(f"Niño/a: menor de 12 años. \n")
elif edad >= 18 and edad < 30:
    print(f"Adulto/a joven: mayor o igual que 18 años y menor que 30 años. \n")
else:
    print(f"Adulto/a: mayor o igual que 30 años. \n")


# Enunciado - Actividad 5
ej_5 = '''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. \n'''
print(ej_5)

# Resolución - Actividad 5
# Solicito ingresar contraseña
password = input("Ingresa tu contraseña: ")
password_len = len(password)
# valido la longitud de la contraseña
if password_len >= 8 and password_len <= 14:
   print(f"“Ha ingresado una contraseña correcta”.\n")
else:
   print(f"“Por favor, ingrese una contraseña de entre 8 y 14 caracteres”.\n")


# Enunciado - Actividad 6
ej_6 = '''6)  El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:

from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)

En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.

La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:

● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.

● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.

● Sin sesgo: cuando la media, la mediana y la moda son iguales.

Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria. \n'''
print(ej_6)

# Resolución - Actividad 6
# importo las librerias a utilizar
from statistics import mode, median, mean
import random
# creo lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# calculo la moda (mode), la mediana (median) y la media (mean)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
sesgoP = media > mediana > moda
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
sesgoN = media < mediana < moda
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
sinSesgo = media == mediana == moda
# comparo e imprimo
if sesgoP:
    print("Sesgo positivo o a la derecha.\n")
elif sesgoN:
    print("Sesgo negativo o a la izquierda.\n")
elif sinSesgo:
    print("Sin sesgo.\n")
else:
    print("No hay un sesgo definido.\n")
    
    
# Enunciado - Actividad 7
ej_7 = '''7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. \n'''
print(ej_7)

# Resolución - Actividad 7
# Solicitar una frase o palabra al usuario
texto = input("Ingresa una frase o palabra: ")
# Verificar si termina en vocal (mayúscula o minúscula)
if texto[-1].lower() in 'aeiou':
    texto += '!'    
# Imprimir el resultado
print("Resultado:", texto)


# Enunciado - Actividad 8
ej_8 = '''8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. \n'''
print(ej_8)

# Resolución - Actividad 8
# Solicitar el nombre al usuario
nombre = input("Ingresá tu nombre: ")
# Solicitar la opción deseada
print("Elegí una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la Primera Letra en Mayúscula")
opcion = input("Ingresá 1, 2 o 3: ")
# Transformar el nombre según la opción seleccionada
if opcion == '1':
    resultado = nombre.upper()
elif opcion == '2':
    resultado = nombre.lower()
elif opcion == '3':
    resultado = nombre.title()
else:
    resultado = "Opción no válida."
# Imprimir el resultado
print("Resultado:", resultado)

# Enunciado - Actividad 9
ej_9 = '''9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). \n'''
print(ej_9)

# Resolución - Actividad 9
# Solicita la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Clasificación según la magnitud
if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"
# Imprimir el resultado
print(f"Clasificación: {clasificacion}")


# Enunciado - Actividad 10
ej_10 = '''10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

Periodo del año	                                        Estación en el hemisferio norte	     Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)	   Invierno	                                 Verano
Desde el 21 de marzo hasta el 20 de junio (incluidos)     	   Primavera	                              Otoño
Desde el 21 de junio hasta el 20 de septiembre (incluidos)	   Verano	                                 Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)	Otoño	                                    Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
qué mes del año es y qué día es. El programa deberá utilizar esa información para 
imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. \n'''
print(ej_10)

# Resolución - Actividad 10
# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (en número, 1-12): "))
dia = int(input("¿Qué día del mes es?: "))

# Determinar estación directamente sin función
if hemisferio == "N":
    # Invierno: del 21 de diciembre al 20 de marzo
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    # Primavera: del 21 de marzo al 20 de junio
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    # Verano: del 21 de junio al 20 de septiembre
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    # Otoño: del 21 de septiembre al 20 de diciembre
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"  # Por si el día ingresado no es coherente
elif hemisferio == "S":
    # Verano: del 21 de diciembre al 20 de marzo
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    # Otoño: del 21 de marzo al 20 de junio
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    # Invierno: del 21 de junio al 20 de septiembre
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    # Primavera: del 21 de septiembre al 20 de diciembre
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no válido"  # Si el usuario no ingresa N o S correctamente

# Mostrar resultado
print(f"Te encontrás en la estación: {estacion}")

