"""
TP - Recursividad
Autor: Damián Jorge Portillo
Materia: Programación I - Tecnicatura Universitaria en Programación a Distancia
"""

# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    print("Serie de Fibonacci:")
    for i in range(hasta):
        print(fibonacci(i), end=" ")
    print()

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Conversión a binario recursiva
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Verificación de palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# 7) Pirámide de bloques recursiva
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar dígitos recursivamente
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Programa principal de prueba
if __name__ == "__main__":
    
    # Enunciado - Actividad 1
    ej_1 = '''\n1) Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de 
todos los números enteros entre 1 y el número que indique el usuario. \n'''
    print(ej_1)

    # Resolución - Actividad 1
    num = int(input("Ingrese un número para calcular factoriales hasta ese número: "))
    mostrar_factoriales(num)

    # Enunciado - Actividad 2
    ej_2 = '''\n2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.  \n'''
    print(ej_2)

    # Resolución - Actividad 2
    num = int(input("Ingrese hasta qué posición desea ver la serie de Fibonacci: "))
    mostrar_fibonacci(num)

    # Enunciado - Actividad 3
    ej_3 = '''\n3)Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.\n'''
    print(ej_3)
    
    # Resolución - Actividad 3
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

    # Enunciado - Actividad 4
    ej_4 = '''\n4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
y devuelva su representación en binario como una cadena de texto. \n'''
    print(ej_4)

    # Resolución - Actividad 4
    decimal = int(input("Ingrese un número decimal positivo: "))
    resultado = decimal_a_binario(decimal)
    print(f"Binario: {resultado if resultado else '0'}")

    # Enunciado - Actividad 5
    ej_5 = '''\n5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed().  \n'''
    print(ej_5)

    # Resolución - Actividad 5
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    print("Es palíndromo." if es_palindromo(palabra) else "No es palíndromo.")

    # Enunciado - Actividad 6
    ej_6 = '''\n6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)  \n'''
    print(ej_6)

    # Resolución - Actividad 6
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Suma de dígitos: {suma_digitos(numero)}")

    # Enunciado - Actividad 7
    ej_7 = '''\n7)  Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 

Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)  \n'''
    print(ej_7)

    # Resolución - Actividad 7
    bloques = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(bloques)}")

    # Enunciado - Actividad 8
    ej_8 = '''\n8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0    \n'''
    print(ej_8)

    # Resolución - Actividad 8
    numero = int(input("Ingrese un número entero positivo: "))
    dig = int(input("Ingrese un dígito (0-9): "))
    print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces. \n")
