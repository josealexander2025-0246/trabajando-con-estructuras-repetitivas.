# Crear un programa que permita capturar n cantidad de ventas y registrar el producto y precio para cada transacción. Mostrar o imprimir cada producto con su preciso


ventas = []

A = int(input("¿Cuántas ventas desea registrar? "))

for i in range(A):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    ventas.append((producto, precio))
print("Resumen de ventas:")
for producto, precio in ventas:
    print(f"Producto: {producto}, Precio: ${precio:.2f}")
total_ventas = sum(precio for producto, precio in ventas)
print(f"Total de ventas: ${total_ventas:.2f}")
