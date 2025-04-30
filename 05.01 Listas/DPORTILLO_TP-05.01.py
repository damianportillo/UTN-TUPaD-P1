print('\nAlumno: Damián Jorge Portillo.\n')
print('Práctico 5.1: Listas. \n')
print('Actividades.\n')

# Enunciado - Actividad 1
ej_1 = '''1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función,range..\n'''
print(ej_1)

# Resolución - Actividad 1
#Creo una lista de los múltiplos de 4 del 1 al 100
multiples_de_4 = list(range(4, 101, 4))
#Muestra la lista resultante
print(multiples_de_4)


Enunciado - Actividad 2
ej_2 = '''2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!. \n'''
print(ej_2)

# Resolución - Actividad 2
# Crear una lista con 5 elementos favoritos
favoritos = ['Python', 'C#', 'C++', 'Java', 'Node']

# Mostrar el penúltimo elemento usando indexación negativa
print("El penúltimo elemento es:", favoritos[-2])


# Enunciado - Actividad 3
ej_3 = '''3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []. \n'''
print(ej_3)

# Resolución - Actividad 3
# Crear una lista vacía
lista_vacia = []
#Agregar tres palabras usando append
lista_vacia.append("Secuenciales")
lista_vacia.append("Condicionales")
lista_vacia.append("Repetitivas")
#Imprimir la lista resultante
print("Lista resultante:", lista_vacia)

# Enunciado - Actividad 4
ej_4 = '''4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]\n'''
print(ej_4)

# Resolución - Actividad 4
# Lista original
animales = ["perro", "gato", "conejo", "pez"]
# Reemplazar el segundo valor (índice 1) por "loro"
animales[1] = "loro"
# Reemplazar el último valor (índice -1) por "oso"
animales[-1] = "oso"
# Imprimir la lista resultante
print("Lista modificada:", animales)


# Enunciado - Actividad 5
ej_5 = '''5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros) \n'''
print(ej_5)

# Resolución - Actividad 5

# Explicación paso a paso:
# 1. Se crea una lista llamada numeros con los valores [8, 15, 3, 22, 7].
# 2. La función: max(numeros), busca el valor máximo de la lista, que en este caso es 22.
# 3. El método remove del array elimina el primer elemento de la lista que coincida con ese valor máximo, numeros.remove(max(numeros)). Es decir, se elimina 22.
# 4. print(numeros) muestra por pantalla la lista actualizada sin el número mayor.

# Resultado en pantalla: 
# [8, 15, 3, 7]

# En resumen:
# El programa elimina el número más grande de la lista numeros y luego imprime la lista resultante.

# Enunciado - Actividad 6
ej_6 = '''6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. \n'''
print(ej_6)

# Resolución - Actividad 6
#Creo una lista del 10 al 30 con saltos de 5
numeros = list(range(10, 31, 5))
#Mostrar los dos primeros elementos
print("Los dos primeros elementos son:", numeros[:2])


# Enunciado - Actividad 7
ej_7 = '''7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"] \n'''
print(ej_7)

# Resolución - Actividad 7
# Lista original
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazar los dos valores centrales (índices 1 y 2)
autos[1] = "mustang"
autos[2] = "civic"
# Imprimir la lista modificada
print("Lista modificada:", autos)


# Enunciado - Actividad 8
ej_8 = '''8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
Imprimir la lista resultante por pantalla. \n'''
print(ej_8)

# Resolución - Actividad 8
# Crear una lista vacía
dobles = []
# Agregar el doble de 5, 10 y 15 usando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
# Imprimir la lista resultante
print("Lista de dobles:", dobles)


# Enunciado - Actividad 9
ej_9 = '''9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla. \n'''
print(ej_9)

# Resolución - Actividad 9
# Lista original de compras.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print("Lista modificada de compras:", compras)

# Salida esperada: 
# Lista modificada de compras: [['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]


# Enunciado - Actividad 10
ej_10 = '''10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla. \n'''
print(ej_10)

# Resolución - Actividad 10
#Crear la lista anidada según las posiciones indicadas
lista_anidada = [
    15,                # lista_anidada[0]
    True,              # lista_anidada[1]
    [25.5, 57.9, 30.6],# lista_anidada[2][0], [2][1], [2][2]
    False              # lista_anidada[3]
]

#Imprimir la lista resultante
print("Lista anidada:", lista_anidada)

# Salida esperada:
# Lista anidada: [15, True, [25.5, 57.9, 30.6], False]