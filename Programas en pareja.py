# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Las asignaturas del curso son:")
print(asignaturas)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio , donde es cada una de las asignaturas de la lista.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for materia in asignaturas:
    print("Yo estudio", materia)

# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En has sacado donde es cada una des las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for materia in asignaturas:
    nota = input("¿Qué nota has sacado en " + materia + "? ")
    notas.append(nota)

print("\nTus resultados son:")
for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])

# Ejercicio 4
# # Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# Ejercicio 4: Números ganadores de la lotería primitiva
numeros = []  # Lista vacía para los números

for i in range(6):
    numero = int(input("Introduce un número ganador: "))
    numeros.append(numero)

numeros.sort()

print("Los números ganadores ordenados son:", numeros)

# Ejercicio 5
# # Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = list(range(1, 11))
numeros.reverse()

print("Números en orden inverso:")
print(", ".join(map(str, numeros)))

# Ejercicio 6
# # Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

for materia in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + materia + "? "))
    if nota < 5:
        repetir.append(materia)


# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

print("\nDebes repetir las siguientes asignaturas:")
print(repetir)

abecedario = list("abcdefghijklmnopqrstuvwxyz")


resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]

print("Abecedario sin letras en posiciones múltiplos de 3:")
print(resultado)


# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


palabra = input("ingrese una palabra: ")

invertida = palabra[::-1]

if palabra == invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")


# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra: ")


vocales = "aeiouAEIOU"

contador = {}
for vocal in vocales:
    contador[vocal] = 0
for letra in palabra:
    if letra in vocales:
        contador[letra] += 1
for vocal, cantidad in contador.items():
    if cantidad > 0:
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")


# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]

menos = precios[0]
mayor = precios[0]

for precio in precios:
    if precio < menos:
        menos = precio
    if precio > mayor:
        mayor = precio

print(f"El precio menor es: {menos}")
print(f"El precio mayor es: {mayor}")


# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.


vect1 = [1, 2, 3]
vect2 = [-1, 0, 2]

producto = 0
for i in range(len(vect1)):
    producto += vect1[i] * vect2[i]

print(f"El producto escalar:{producto}")

# Ejercicio 12
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


E = input("Ingresa una muestra de números separados por comas: ")

numeros = E.split(",")
numeros = [float(num) for num in numeros]
media = sum(numeros) / len(numeros)

suma = sum((num - media) ** 2 for num in numeros)
desviacion = (suma / len(numeros)) ** 0.5

print(f"La media es: {media}")
print(f"La desviación típica es: {desviacion}")
