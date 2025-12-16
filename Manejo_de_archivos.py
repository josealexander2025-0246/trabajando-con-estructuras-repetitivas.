# crear un programa que permita crear, leer y actualizar archivos de texto.

# El archivo debe tener la siguiente estructura:

# NOMBRE: XXXXX

# MATRICULA: XXXXXX

# CORREO: XXXXXX

# TELEFONO: XXXXXXX

# Crea un menu de opciones con las siguientes opciones:

# archivo
# registros
# leer archivo
# actualizar nombre ( permite escribir un nombre y lo busca en el archivo para reemplazarlo con otro valor)
# cerrar
# Subir a github

import os

nombre_del_archivo = ""


def crear_archivo():
    global nombre_del_archivo
    nombre = input("Escribe el nombre del archivo (sin extensión): ")
    nombre_del_archivo = nombre + ".txt"

    with open(nombre_del_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("# ARCHIVO DE ESTUDIANTES\n")
        archivo.write("# " + "=" * 50 + "\n\n")

    print(f" Archivo '{nombre_del_archivo}' creado")


def guardar_registros():
    if nombre_del_archivo == "":
        print(" Error: Primero debes crear un archivo")
        return

    print(" NUEVO REGISTRO DE ESTUDIANTE")
    nombre = input("NOMBRE: ")
    matricula = input("MATRICULA: ")
    correo = input("CORREO: ")
    telefono = input("TELEFONO: ")

    if nombre == "" or matricula == "" or correo == "" or telefono == "":
        print(" Error: Todos los campos son obligatorios")
        return

    with open(nombre_del_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"NOMBRE: {nombre}\n")
        archivo.write(f"MATRICULA: {matricula}\n")
        archivo.write(f"CORREO: {correo}\n")
        archivo.write(f"TELEFONO: {telefono}\n")
        archivo.write("-" * 50 + "\n")

    print("Registro guardado correctamente")


def leer_archivo():
    if nombre_del_archivo == "" or not os.path.exists(nombre_del_archivo):
        print("Error: El archivo no existe o no ha sido definido.")
        return

    with open(nombre_del_archivo, "r", encoding="utf-8") as archivo:
        print("\n--- CONTENIDO DEL ARCHIVO ---")
        print(archivo.read())


def actualizar_nombre():
    if nombre_del_archivo == "":
        print("Primero define un archivo.")
        return

    buscar = input("Nombre exacto que quieres cambiar: ")
    nuevo = input("Nuevo nombre: ")

    with open(nombre_del_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    encontrado = False
    with open(nombre_del_archivo, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            if linea.strip() == f"NOMBRE: {buscar}":
                archivo.write(f"NOMBRE: {nuevo}\n")
                encontrado = True
            else:
                archivo.write(linea)

    if encontrado:
        print("Nombre actualizado.")
    else:
        print("No se encontró ese nombre.")


while True:
    print("\n--- MENÚ DE ESTUDIANTES ---")
    print("1. Crear archivo")
    print("2. Guardar registro")
    print("3. Leer archivo")
    print("4. Actualizar nombre")
    print("5. Cerrar")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_archivo()
    elif opcion == "2":
        guardar_registros()
    elif opcion == "3":
        leer_archivo()
    elif opcion == "4":
        actualizar_nombre()
    elif opcion == "5":
        print("bye")
        break
    else:
        print("Opción inválida")
