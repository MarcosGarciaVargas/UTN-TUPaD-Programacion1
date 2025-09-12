import random

# Ejercicio 1 

lista_nota_estudiantes = [6,10,5,8,1,8,9,10,4,7]#establezco notas
#inicializo variables
num_estudiante = 1#contador del estudiante
promedio_notas = 0
nota_mas_alta = 0
nota_mas_baja = float("inf")

for i in lista_nota_estudiantes:#bucle for, recorre la lista de notas
    print(F"Nota del estudiante num-{num_estudiante} : {i}")
    num_estudiante += 1#va sumando cada iteracion para que cambie de estudiante
    promedio_notas += i#le asigno su nota 
    if i > nota_mas_alta:#si la nota es la mas alta, actualizo la variable
        nota_mas_alta = i
    if i < nota_mas_baja:#si la nota es la mas baja, actualizo la variable
        nota_mas_baja = i
print("")
promedio_final_notas = (promedio_notas/10)#saco el promedio diviendo por 10
print(f"El promedio final es : {promedio_final_notas}")
print(f"La nota mas alta es : {nota_mas_alta}")
print(f"La nota mas baja es : {nota_mas_baja}")
print("")

# Ejercicio 2

contador_productos = 5#variable con cantidad de productos
lista_productos = []#inicializo la lista

while contador_productos != 0:#mientras el contador sea distinto a 0
    pregunta_cinco_productos = (input("Ingrese un producto a la lista :"))#pido un valor al usuario
    contador_productos -= 1#le resto al contador 

    lista_productos.append(pregunta_cinco_productos)#sumo el input a la lista
print(sorted(lista_productos))#sorted acomoda la lista segun su orden alfabetico

producto_a_eliminar = (input("Que producto desea eliminar? :"))#pido un input
if producto_a_eliminar in lista_productos:#me aseguro que el producto existe
    lista_productos.remove(producto_a_eliminar)#remove sirve para quitar un valor de la listaw
else:
    print("El producto no es parte de la lista")
print("")
#print(sorted(lista_productos))  no entendí si era necesario mostrarlo luego de actualizar

# Ejercicio 3
#inicializo listas y variables
lista_numeros_random = []

cantidad_de_random = 15
num_random_pares = []
num_random_impares = []

for i in range(cantidad_de_random):#desde i hasta 15
    numero_random = random.randint(1,100)#uso la funcion randint
    lista_numeros_random.append(numero_random)#agrego los numeros aleatorios a la lista
    if numero_random%2 == 0:#si el resto es 0
        num_random_pares.append(numero_random)#lo agrego a la lista de pares
    else:
        num_random_impares.append(numero_random)#en caso contrario a la de imparess
#muestro por consola
print(f"lista con todos los numeros{lista_numeros_random}")
print(f"Numeros par :{num_random_pares}")
print(f"Numero impar :{num_random_impares}")
print("")
# Ejercicio 4
#inicializo listas
datos = [1,3,5,3,7,1,9,5,3]

datos_sin_repetidos = []

for i in datos:#recorro la lista bucle for
    if i not in datos_sin_repetidos:#si NO esta el numero en la lista, lo agrega
        datos_sin_repetidos.append(i)
#muestro la lista sin numeros repetidos
print(f"lista sin numeros repetidos :{datos_sin_repetidos}")
print("")
# Ejercicio 5
#inicializo lista
Lista_de_alumnos = ["Pedro", "Juan", "Maria", "Lucas", "Sofia", "Eduardo", "Agustina", "Facundo"]
#pido un input str
modificar_estudiante = str(input("Desea Agregar o Eliminar algun estudiante existente? A/E :"))

if modificar_estudiante == "A" or modificar_estudiante == "a":#evito un error de valor
    estudiante_agregar = str(input("Cual es el nombre del estudiante que desea agregar? :"))#pido un input
    Lista_de_alumnos.append(estudiante_agregar)#agrego el str a la lista
elif modificar_estudiante == "E" or modificar_estudiante == "e":
    estudiante_eliminar = str(input("Cual es el nombre del estudiante que desea eliminar? :"))#pido input str
    Lista_de_alumnos.remove(estudiante_eliminar)#remuevo el elemento de la lista
#muestro en consola
print("")
print(f"La lista final es {Lista_de_alumnos}")

print("")
# Ejercicio 6
#inicializo lista
Lista_siete_numeros = [5,6,4,2,7,3,1]
#uso la función len para determinar el largo de la lista
cantidad_elementos = len(Lista_siete_numeros)

for indice_actual in range(cantidad_elementos - 1, 0, -1):#muevo el ultimo numero de la lista hacia atras, y frena en el 0 osea la ultima posición
   Lista_siete_numeros[indice_actual], Lista_siete_numeros[indice_actual - 1] = Lista_siete_numeros[indice_actual - 1], Lista_siete_numeros[indice_actual]
    #agarro variables de 2 en 2 , cambian lugares con el 1 del final hasta que este llegue al principio
print(f"Numeros reordenados : {Lista_siete_numeros}")

print("")
# Ejercicio 7
#inicializo variables
suma_mintemp = 0
suma_maxtemp = 0

mayor_temperatura = float("-inf")
menor_temperatura = float("inf")
#7 filas y 2 columnas
matriz_temperaturas = [
    [3,14],
    [5,18],
    [2,10],
    [7,15],
    [8,15],
    [7,18],
    [6,17]
]
for fila in matriz_temperaturas:#por cada fila en la matriz
    suma_mintemp += fila[0]#sumo el primer elemento a la variable
for fila in matriz_temperaturas:#por cada fila en la matriz
    suma_maxtemp += fila[1]#sumo el segundo elemento a la variable

for fila in matriz_temperaturas:#por cada fila en la matriz

    if fila[1] > mayor_temperatura:#si el elemento 2 es mayor a la variable "mayor_temperatura"
        mayor_temperatura = fila[1]#se actualiza su valor
    elif fila[0] < menor_temperatura:#si el elemento 1 es menor a la variable "menor_temperatura"
        menor_temperatura = fila[0]#se actualiza su valor

promedio_minima = suma_mintemp/7#saco el promedio minima
promedio_maxima = suma_maxtemp/7#saco el promedio maxima
print(f"La temperatura Minima es {round(promedio_minima,1)}")#con round hago que solo se vea 1 valor despues de la coma
print(f"La temperatura Maxima es {round(promedio_maxima,1)}")#
print("")
print(f"la temperatura Maxima esa semana fue :{mayor_temperatura}")
print(f"La menor temperatura esa semana fue : {menor_temperatura}")
print("")
# Ejercicio 8

#matriz 5 filas 3 columnas
matriz_estudiantes =[
    [6, 8, 9],
    [10, 10, 9],
    [7, 8, 8],
    [4, 5, 4],
    [7, 10, 6]
]

contador_notas = 1#inicializo contador
for fila in matriz_estudiantes:#por cada fila en la matriz
    suma_notas = fila[0] + fila[1] + fila[2]#agarro los 3 elementos y los sumo a una variable
    #hago el promedio dividiendo la suma por 3, y uso round para que solo tenga 1 numero luego de la coma
    (print(f"Promedio de estudiante num-{contador_notas} : {round(suma_notas/3,1)}"))
    contador_notas += 1#aumento el contador para pasar de alumno
#inicializo variables
materia_1 = 0
materia_2 = 0
materia_3 = 0

for fila in matriz_estudiantes:#por cada fila de la matriz
    materia_1 += fila[0]#sumo el elemento 1
    materia_2 += fila[1]#sumo el elemento 2 
    materia_3 += fila[2]#sumo el elemento 3
print("")
#muestro en pantalla
print(f"El promedio de la primer materia es {(materia_1/5)}")
print(f"El promedio de la segunda materia es {(materia_2/5)}")
print(f"El promedio de la tercer materia es {(materia_3/5)}")
print("")

# Ejercicio 9
#3x3 3 filas 3 columnas
tablero_juego = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

for i in tablero_juego:#por cada elemento del tablero lo muestro en consola
    print(i)

for turno in range(9):#por cada turno en un rango de 9 (ya que son 9 casilleros)
    if turno%2 == 0:#si el turno es par es turno de O
        jugador = "O"
    else:#caso contrario es turno de X
        jugador = "X"

    fila = int(input("Ingrese un numero de fila (0-1-2) :"))#pido un input entre 0 y 2
    columna = int(input("Ingrese un numero de columna (0-1-2) :"))#pido un input entre 0 y 2

    if tablero_juego[fila][columna] == "-":#si la fila que el usuario decidio esta vacia "-"
        tablero_juego[fila][columna] = jugador#se reemplaza por el valor del jugador
    else:
        print("ERROR: esta casilla ya esta ocupada")#caso contrario el programa sigue

    for fila in tablero_juego:#muestro la tabla actualizada
        print(fila)
print("")
# Ejercicio 10
#inicializo variables
ventas_prod_uno = 0
ventas_prod_dos = 0
ventas_prod_tres = 0
ventas_prod_cuatro = 0

dia_mas_ventas = 0
contador = 0
producto_mas_vendido = ""
#matriz 4 columnas 7 filas
ventas_semana = [
    [23, 5, 11, 18],
    [22, 8, 12, 17],
    [21, 8, 15, 21],
    [25, 4, 17, 24],
    [29, 9, 15, 28],
    [19, 3, 16, 31],
    [31, 11, 10, 38]
]

for fila in ventas_semana:#recorro cada fila
    ventas_prod_uno += fila[0]#sumo el elemento 1 a su variable
    ventas_prod_dos += fila[1]#sumo el elemento 2 a su variable
    ventas_prod_tres += fila[2]#sumo el elemento 3 a su variable
    ventas_prod_cuatro += fila[3]#sumo el elemento 4 a su variable

if (ventas_prod_uno > ventas_prod_dos and ventas_prod_uno > ventas_prod_tres and ventas_prod_uno > ventas_prod_cuatro):
    producto_mas_vendido = "El Producto 1"#si ventas prod 1 son mayores a todas las demas
elif (ventas_prod_dos > ventas_prod_tres and ventas_prod_dos > ventas_prod_cuatro):
    producto_mas_vendido = "El Producto 2"#si ventas prod 2 son mayores a todas las demas
elif ventas_prod_tres > ventas_prod_cuatro:
    producto_mas_vendido = "El Producto 3"#si ventas prod 3 son mayores a todas las demas
else:
    producto_mas_vendido = "El Producto 4"#si ventas prod 4 son mayores a todas las demas

dia_actual = 1#inicializo variable con dia 1
for fila in ventas_semana:#recorro cada fila de la matriz
    ventas_dia = 0#inicializo ventas_dia =0
    for ventas in fila:#voy tomando los valores por cada dia
        ventas_dia += ventas

    if ventas_dia > dia_mas_ventas:#si las ventas de ese dia son mayores a el dia con mas ventas
        dia_mas_ventas = ventas_dia#intercambio las variables
        contador = dia_actual#contador va guardando cada iteracion
    dia_actual += 1#dia actual se actualiza cuando realmente se actualiza el dia mayor, si no, sigue en 1 

#muestro por consola
print(f"en total se vendieron '{ventas_prod_uno}' del primer producto")
print(f"en total se vendieron '{ventas_prod_dos}' del segundo producto")
print(f"en total se vendieron '{ventas_prod_tres}' del tercer producto")
print(f"en total se vendieron '{ventas_prod_cuatro}' del cuarto producto")
print("")
print(f"El dia que mas ventas hubo fue el dia {contador}")
print(f"El producto mas vendido fue {producto_mas_vendido}")
