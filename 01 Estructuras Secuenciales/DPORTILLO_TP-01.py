import math

print('\nAlumno: Damián Jorge Portillo.\n')
print('Unidad 1 - Estructuras Secuenciales.\n')
print('Actividades.\n')

# Enunciado - Actividad 1
ej_1 = '''1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.\n'''
print(ej_1)

# Resolución - Actividad 1
print(f'“Hola Mundo!”\n')

# Enunciado - Actividad 2
ej_2 = '''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. \n'''
print(ej_2)

# Resolución - Actividad 2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!\n")

# Enunciado - Actividad 3
ej_3 = '''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. \n'''
print(ej_3)

# Resolución - Actividad 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"“Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}”.\n")

# Enunciado - Actividad 4
ej_4 = '''4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.  \n'''
print(ej_4)

# Resolución - Actividad 4
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}\n")

# Enunciado - Actividad 5
ej_5 = '''5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale.   \n'''
print(ej_5)

# Resolución - Actividad 5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos // 3600 
minutos = (segundos % 3600) // 60
print(f"{segundos} segundos equivalen a {horas} hora(s) y {minutos} minuto(s).\n")

# Enunciado - Actividad 6
ej_6 = '''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número. \n'''
print(ej_6)

# Resolución - Actividad 6
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print('\n')

# Enunciado - Actividad 7
ej_7 = '''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.  \n'''
print(ej_7)

# Resolución - Actividad 7
print("Se solicita ingresar dos números enteros distintos del 0.\n")
numeroUno = 0
numeroDos = 0

while numeroUno == 0 :
    numeroUno = int(input("Ingrese el primer número:"))
    
while numeroDos == 0 :
    numeroDos = int(input("Ingrese el segundo número:"))
    
print(f"\n{numeroUno} + {numeroDos} = {numeroUno+numeroDos}")
print(f"{numeroUno} - {numeroDos} = {numeroUno-numeroDos}")  
print(f"{numeroUno} * {numeroDos} = {numeroUno*numeroDos}")  
print(f"{numeroUno} / {numeroDos} = {numeroUno/numeroDos:.2f} \n")

# Enunciado - Actividad 8
ej_8 = '''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
modo:  

𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2\n'''
print(ej_8)

# Resolución - Actividad 8
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)
print(f"\nTu índice de masa corporal (IMC) es: {imc:.2f}\n")

# Enunciado - Actividad 9
ej_9 = '''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠  + 32 \n'''
print(ej_9)

# Resolución - Actividad 9
celsius = float(input("Introduce la temperatura en grados Celsius: "))
# Calcular la temperatura en Fahrenheit
fahrenheit = (9/5) * celsius + 32
print(f"\nLa temperatura en grados Fahrenheit es: {fahrenheit:.2f}\n")

# Enunciado - Actividad 10
ej_10 = '''10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números.  \n'''
print(ej_10)

# Resolución - Actividad 10
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
# Calcular el promedio
promedio = (numero1 + numero2 + numero3) / 3
print(f"\nEl promedio de los tres números es: {promedio:.2f}\n")


