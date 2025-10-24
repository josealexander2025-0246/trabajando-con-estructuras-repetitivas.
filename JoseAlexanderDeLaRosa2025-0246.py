"""
Nombre: Jose Alexander De La Rosa Jimenez
Matrícula: 2025-0246
Fecha: 20/10/2025
Ejercicios de Bucles (For y While)
"""

# EJERCICIO 1: Imprimir números del 1 hasta N
# Escribe un programa que pida al usuario que ingrese un número entero positivo.
# El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno,
# utilizando un bucle while.


limite = int(input("Ingresa un número entero positivo: "))
contador = 1

while contador <= limite:
    print(contador)
    contador = contador + 1


# EJERCICIO 2: Números pares del 1 al 20
# Escribe un programa que imprima los números pares entre 1 y 20 (inclusive) utilizando un bucle for.


for numerito in range(1, 21):
    if numerito % 2 == 0:
        print(numerito)


# EJERCICIO 3: Contar dígitos
# Escribe un programa que pida al usuario un número entero positivo.
# El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.


numero = int(input("Ingresa un número entero positivo: "))
original = numero
digitos = 0

while numero > 0:
    numero = numero // 10
    digitos = digitos + 1

print(f"El número {original} tiene {digitos} dígitos")


# EJERCICIO 4: Suma del 1 al 100
# Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for.


suma = 0

for numerito in range(1, 101):
    suma = suma + numerito

print(f"La suma de todos los números del 1 al 100 es: {suma}")


# EJERCICIO 5: Cuenta regresiva
# Escribe un programa que pida al usuario un número entero y luego imprima todos
# los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.


numero = int(input("Ingresa un número para empezar la cuenta regresiva: "))

while numero >= 0:
    print(numero)
    numero = numero - 1

print("¡Despegue!")


# EJERCICIO 6: Tabla de multiplicar
# Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario,
# desde el 1 hasta el 10, utilizando un bucle for.


base = int(input("¿De qué número quieres la tabla de multiplicar? "))

for multi in range(1, 11):
    resultado = base * multi
    print(f"{base} x {multi} = {resultado}")


# EJERCICIO 7: Números impares
# Escribe un programa que pida al usuario un número entero positivo y luego imprima
# todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.


limite = int(input("Ingresa un número entero positivo: "))
impar = 1

while impar <= limite:
    print(impar)
    impar = impar + 2


# EJERCICIO 8: Serie de Fibonacci
# Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término,
# donde el valor de n lo ingresa el usuario, utilizando un bucle for.


terminos = int(input("¿Cuántos términos de Fibonacci quieres? "))

primero = 0
segundo = 1

print(primero)
if terminos > 1:
    print(segundo)

for i in range(2, terminos):
    siguiente = primero + segundo
    print(siguiente)
    primero = segundo
    segundo = siguiente


# EJERCICIO 9: Factorial
# Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while.
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.


numero = int(input("Ingresa un número para calcular su factorial: "))
original = numero
factorial = 1
contador = 1

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1

print(f"El factorial de {original} es: {factorial}")


# EJERCICIO 10: Sistema de contraseña
# Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud
# mientras la contraseña ingresada sea incorrecta. El programa debe continuar hasta que
# el usuario ingrese la contraseña correcta. Utiliza una estructura while para simular un do while.


clave = "ronoroaz123"
intento = ""

while intento != clave:
    intento = input("Ingresa la contraseña: ")
    if intento != clave:
        print("Contraseña incorrecta. Intenta de nuevo.")
    else:
        print("Acceso concedido")
