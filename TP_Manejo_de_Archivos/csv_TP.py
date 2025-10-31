import os
#supuse que habia que crear el "productos.txt" con la función open, use el modulo os para que no se sobreescriba el txt

# Ejercicio 1 

#abro el archivo de texto "productos.txt", si no existe lo creo
if not os.path.exists("productos.txt"):
    with open("productos.txt", "w") as archivo_inicial:
        archivo_inicial.write("Pera,2000,30\n")#agrego los valores predeterminados
        archivo_inicial.write("Manzana,1550,25\n")
        archivo_inicial.write("Naranja,2420,18\n")

# Ejercicio 2

with open("productos.txt", "r") as archivo_inicial:
    for linea in archivo_inicial:#por cada linea en el txt
        linea = linea.strip().split(",")#recorro cada linea, quito espacios y divido elementos por coma
        print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")

# Ejercicio 3

nuevo_producto = input("\nIngrese un nuevo producto (separado por ,):")#pido input de usuario
datos_producto = nuevo_producto.strip().split(",")#separo por comas y saco espacios

if len(datos_producto) == 3:#si la palabra ingresada tiene 3 palabras
    with open("productos.txt", "a") as archivo_inicial:
        archivo_inicial.write(nuevo_producto + "\n")
else:#en cualquier otro caso, error
    print("Error")

# Ejercicio 4

productos = []
#inicializo lista y leo el txt 
with open("productos.txt", "r") as archivo_inicial:
    for linea in archivo_inicial:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({#paso los productos desde el txt a la lista
            "nombre": nombre, 
            "precio" : precio, 
            "cantidad" : cantidad})

# Ejercicio 5

nombre_buscado = input("\nIngrese el nombre del producto que desea encontrar: ")
#le pido al usuario un input, y recorro la lista productos
for producto in productos:
    if producto["nombre"].lower() == nombre_buscado.lower():#si coincide el nombre ingresado con alguno en la lista
        print("\nSe encontro el producto!!")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        break #corto la ejecucion para evitar duplicidad de mensajes de error
else:
    print("Error, ese producto no fue encontrado")


# Ejercicio 6

#limpio la lista productos
productos = []

with open("productos.txt", "r") as archivo_actualizado:
    for linea in archivo_actualizado:
        nombre,precio,cantidad = linea.strip().split(",")
        #agrego cada producto del txt a la lista como diccionario
        productos.append({"nombre" : nombre, "precio" : precio, "cantidad" :cantidad})

with open("productos.txt", "w") as archivo_actualizado:
    #sobrescribo cada producto con formato CSV en el txt
    for producto in productos:
        linea = (f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        archivo_actualizado.write(linea)