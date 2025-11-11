# Clasificación de ángulos Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).


grados = float(input("Por favor, ingrese el valor: "))

if grados < 90:
    print("El ángulo es agudo.")
elif grados == 90:
    print("El ángulo es recto.")
elif grados > 90 and grados < 180:
    print("El ángulo es obtuso.")
elif grados == 180:
    print("El ángulo es llano.")
else:
    print("El valor ingresado no es un ángulo válido.")
