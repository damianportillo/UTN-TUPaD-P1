"""
Trabajo Práctico 6 - Estructuras de datos complejas 
Autor: Damián Jorge Portillo
Materia: Programación I
Carrera: Tecnicatura Universitaria en Programación a Distancia
Institución: Universidad Tecnológica Nacional (UTN)
"""

# Funciones

# 1) funcion para combinar diccionarios
def agregar_diccionario(dic, add_dic):
    dic.update(add_dic)

# 2) actualizar keys existentes de un diccionario
def actualizar_diccionario(dic, add_dic):
    for clave, nuevo_valor in add_dic.items():
        if clave in dic:
            dic[clave] = nuevo_valor

# 3) devuelve lista con las claves de un diccionario
def claves_diccionario_a_lista(dic):
    return list(dic.keys())    

# 4) crear diccionario con valor y clave
def crear_diccionario(clave, valor):
    """Crea un diccionario con una clave y un valor dados."""
    return {clave: valor}
# 4) obtener de un diccionario el valor pasando la clave
def valor_diccionario_por_clave(dic, clave):
    """Busca un valor en el diccionario usando la clave. Si no existe, retorna None."""
    return dic.get(clave, None)

# 5) recibe frase la divide y con ellas devuelve un set y diccionario con sus cantidades
def palabras_unicas_y_recuento(frase):
    palabras = frase.lower().split()  # Convertir a minúsculas y dividir en palabras
    palabras_unicas = set(palabras)  # Obtener palabras únicas con un set
    recuento = {}  # Diccionario para contar las palabras
    
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1
    
    return palabras_unicas, recuento

# 6) solicita 3 nombres de alumnos y sus 3 notas, devuelve dic con esos datos
def ingresar_alumnos_y_notas():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)  # Guardamos las notas como tupla
    return alumnos
# 6) recibe dic con alumnos y 3 notas, y devuelve dic con nombre y promedios
def calcular_promedios(alumnos):
    promedios = {}
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        promedios[nombre] = promedio
    return promedios

# 8) gestion de stock, recibe un dic de productos 
def gestionar_stock(stock):  
    while True:
        print("\n--- Gestión de Stock ---")
        print("1. Consultar Stock")
        print("2. Añadir Cantidad")
        print("3. Nuevo Producto")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ").lower()
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]} unidades")
            else:
                print(f"El producto '{producto}' no existe en el stock.")
        
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ").lower()
            if producto in stock:
                try:
                    cantidad = int(input("Ingrese la cantidad a añadir: "))
                    stock[producto] += cantidad
                    print(f"Stock actualizado: ahora tiene {stock[producto]} unidades de {producto}.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
            else:
                print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
        
        elif opcion == "3":
            producto = input("Ingrese el nombre del nuevo producto: ").lower()
            if producto not in stock:
                try:
                    cantidad = int(input("Ingrese el stock inicial: "))
                    stock[producto] = cantidad
                    print(f"Producto '{producto}' añadido con {cantidad} unidades.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
            else:
                print(f"El producto '{producto}' ya existe en el stock.")
        
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# 9) gestion de agenda, recibe un dic de la agenda actual 
def gestionar_agenda(agenda):    
    while True:
        print("\n--- Agenda de Eventos ---")
        print("1. Consultar evento")
        print("2. Agregar evento")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            dia = input("Ingrese el día (ej: lunes): ").lower()
            hora = input("Ingrese la hora (ej: 10:00): ").strip()
            clave = (dia, hora)
            if clave in agenda:
                print(f"Evento: {agenda[clave]}")
            else:
                print("No hay eventos programados para ese día y hora.")
        
        elif opcion == "2":
            dia = input("Ingrese el día (ej: martes): ").lower()
            hora = input("Ingrese la hora (ej: 15:00): ").strip()
            evento = input("Ingrese el evento: ").strip()
            clave = (dia, hora)
            if clave in agenda:
                print("¡Ya existe un evento en ese horario!")
            else:
                agenda[clave] = evento
                print("Evento agregado correctamente.")
        
        elif opcion == "3":
            print("Saliendo de la agenda...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
            


# Programa principal
if __name__ == "__main__":
    
    # Enunciado - Actividad 1
    ej_1 = '''\n1) Dado el diccionario precios_frutas
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    Añadir las siguientes frutas con sus respectivos precios:
    ● Naranja = 1200
    ● Manzana = 1500
    ● Pera = 2300 \n'''
    print(ej_1)

    # Resolución - Actividad 1
    # Diccionario original
    precios_frutas = {
        'Banana': 1200,
        'Ananá': 2500,
        'Melón': 3000,
        'Uva': 1450
    }

    # Nuevas frutas a agregar
    nuevas_frutas = {
        'Naranja': 1200,
        'Manzana': 1500,
        'Pera': 2300
    }

    # Llamado a la función
    agregar_diccionario(precios_frutas, nuevas_frutas)
    # Ver resultado
    print(precios_frutas)
    
    
    # Enunciado - Actividad 2
    ej_2 = '''\n2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
    ● Banana = 1330
    ● Manzana = 1700
    ● Melón = 2800 \n'''
    print(ej_2)

    # Resolución - Actividad 2
    # Diccionario con los nuevos precios
    precios_actualizados = {
        'Banana': 1330,
        'Manzana': 1700,
        'Melón': 2800
    }

    # Llamar a la función para actualizar
    actualizar_diccionario(precios_frutas, precios_actualizados)
    # Ver resultado final
    print(precios_frutas)
    
    
    # Enunciado - Actividad 3
    ej_3 = '''\n3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
    desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
    precios. \n'''
    print(ej_3)
    
    # Resolución - Actividad 3
    # Llamada a la función con el diccionario precios_frutas
    lista_frutas = claves_diccionario_a_lista(precios_frutas)
    # Ver resultado final
    print(lista_frutas)
    
    
    # Enunciado - Actividad 4
    ej_4 = '''\n4) Escribí un programa que permita almacenar y consultar números telefónicos.
    • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
    • Luego, pedí un nombre y mostrale el número asociado, si existe. \n'''
    print(ej_4)

    # Resolución - Actividad 4
    # Cargar 5 contactos en un diccionario
    contactos = {}

    print("Ingrese el nombre y número de 5 contactos:")
    for i in range(5):
        nombre = input(f"Nombre del contacto {i+1}: ")
        telefono = input(f"Número de teléfono de {nombre}: ")
        agregar_diccionario(contactos, crear_diccionario(nombre, telefono))
        
    print("\nDiccionario de contactos:")
    print(contactos)

    # Consultar un contacto
    nombre_busqueda = input("\nIngrese el nombre del contacto a buscar: ")
    resultado = valor_diccionario_por_clave(contactos, nombre_busqueda)

    if resultado is not None:
        print(f"El número de {nombre_busqueda} es: {resultado}")
    else:
        print("Contacto inexistente.")
        
    
    # Enunciado - Actividad 5
    ej_5 = '''\n5) Solicita al usuario una frase e imprime:
    • Las palabras únicas (usando un set).
    • Un diccionario con la cantidad de veces que aparece cada palabra. \n'''
    print(ej_5)

    # Resolución - Actividad 5
    frase_usuario = input("Ingrese una frase: ")
    unicas, recuento = palabras_unicas_y_recuento(frase_usuario)

    print("\nEntrada:", frase_usuario)
    print("\nSalida:")
    print("Palabras_únicas:", unicas)
    print("Recuento:", recuento)   


    # Enunciado - Actividad 6
    ej_6 = '''\n6) Permití ingresar los nombres de 3 alumnos, 
    y para cada uno una tupla de 3 notas.
    Luego, mostrá el promedio de cada alumno.\n'''
    print(ej_6)

    # Resolución - Actividad 6
    alumnos = ingresar_alumnos_y_notas()
    promedios = calcular_promedios(alumnos)
    
    print("\nAlumnos y notas ingresadas:")
    print(alumnos)
    
    print("\nPromedios de los alumnos:")
    for nombre, promedio in promedios.items():
        print(f"Alumno: {nombre}, Promedio: {promedio:.2f}")
    
    
    # Enunciado - Actividad 7
    ej_7 = '''\n7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
    • Mostrá los que aprobaron ambos parciales.
    • Mostrá los que aprobaron solo uno de los dos.
    • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir) \n'''
    print(ej_7)

    # Resolución - Actividad 7
    # Sets de números que representan estudiantes (por ejemplo, por su número de legajo)
    parcial_1 = {101, 102, 103, 104, 105}
    parcial_2 = {104, 105, 106, 107}
    print("Estudiantes que aprobaron parcial 1:", parcial_1)
    print("Estudiantes que aprobaron parcial 2:", parcial_2)

    # A) Estudiantes que aprobaron ambos parciales (intersección)
    ambos = parcial_1 & parcial_2
    print("\nEstudiantes que aprobaron ambos parciales:", ambos)

    # B) Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
    solo_uno = parcial_1 ^ parcial_2
    print("Estudiantes que aprobaron solo uno de los dos:", solo_uno)

    # C) Estudiantes que aprobaron al menos un parcial (unión)
    al_menos_uno = parcial_1 | parcial_2
    print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)


    # Enunciado - Actividad 8
    ej_8 = '''\n8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
    Permití al usuario:
    • Consultar el stock de un producto ingresado.
    • Agregar unidades al stock si el producto ya existe.
    • Agregar un nuevo producto si no existe.\n'''
    print(ej_8)

    # Resolución - Actividad 8
    # dic con stock de productos
    stock = {
        "manzanas": 50,
        "bananas": 30,
        "peras": 20
    }
    
    
    # invoco funcion de gestion de stock y paso dic del stock
    gestionar_stock(stock)
    
    
    # Enunciado - Actividad 9
    ej_9 = '''\n9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
    Ejemplo:
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }

    Permití consultar qué actividad hay en cierto día y hora. \n'''
    print(ej_9)

    # Resolución - Actividad 9
    # dic con dia hora y evento de la agenda
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }
    
    # invoco funcion de gestion de agenda, le paso dic de la agenda actual
    gestionar_agenda(agenda)
    
    
    
    # Enunciado - Actividad 10
    ej_10 = '''\n10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
    diccionario donde:
    • Las capitales sean las claves.
    • Los países sean los valores.
    Ejemplo:
    original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
    invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"} \n'''
    print(ej_10)

    # Resolución - Actividad 10
    # Diccionario original de países y capitales
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción"
    }

    # Invertir el diccionario: capitales como claves, países como valores
    invertido = {capital: pais for pais, capital in original.items()}

    # Mostrar el resultado
    print("Diccionario original:", original)
    print("Diccionario invertido:", invertido)
