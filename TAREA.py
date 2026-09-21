# Programa: Cálculo del precio total de una compra
# Autor: Diego Guapi

def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


print("=== CÁLCULO DEL TOTAL DE UNA COMPRA ===")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad de productos: "))

total_compra = calcular_total(precio, cantidad)

print("\n=== RESULTADO ===")
print("Producto:", producto)
print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("Total a pagar: $", round(total_compra, 2))
