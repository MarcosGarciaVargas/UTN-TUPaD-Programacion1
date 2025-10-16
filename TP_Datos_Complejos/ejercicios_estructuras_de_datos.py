# Ejercicio 1 

#inicializo el diccionario con valores
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

print("Diccionario original :")
print(precios_frutas)#muestro valores iniciales

#agrego frutas con sus valores a el diccionario
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("\n""Diccionario con frutas agregadas :")
print(precios_frutas)#muestro el diccionario actualizado
print("\n")

# Ejercicio 2

print("---"*23)
print("")
print("Diccionario con precios modificados :")
#en este caso actualizo valores ya existentes
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas) #muestro el diccionario con los nuevos valores
print("\n")

# Ejercicio 3

print("Diccionario con solo las frutas :")
diccionario_frutas = [] #inicializo lista
#apunto a las keys osea las frutas de "precios_frutas" y lo paso a lista
diccionario_frutas = list(precios_frutas.keys())

print(diccionario_frutas) #muestro lista en pantalla

# Ejercicio 4

print("\n")
contactos = {} #inicializo el diccionario

for x in range(5):#continuo el bucle hasta que se ingresen 5 contactos

    nombre_contacto = input("Ingrese el nombre del contacto: ")#pido nombre
    numero_contacto = input("Ingrese el número del contacto: ")#pido número
    print("")
    contactos[nombre_contacto] = numero_contacto #lo agrego al diccionario

consulta = input("\nIngrese el nombre del contacto Que desea buscar: ") #pido valor al usuario
#si el valor ingresado se encuentra en el diccionario
if consulta in contactos:
    print(f"El número asociado a {consulta} es {contactos[consulta]}") #muestro en pantalla
else:
    print("Ese contacto no esta almacenado")

# Ejercicio 5

frase = input("\nIngrese una frase :").upper() #pido un str y lo paso a mayúsculas
frase_dividida = frase.split() #divido la frase por cada palabra con la función split

palabras_unicas = set(frase_dividida) #palabras_unicas le asigno el las palabras en un set
print("")
print(f"Las palabras únicas son {palabras_unicas}")
#muestro en pantalla, y el set quita los duplicados

palabras_cantidad = {} #inicializo diccionario
for i in frase_dividida: #por cada palabra de la frase
    if i in palabras_cantidad: 
        palabras_cantidad[i] += 1 #si ya está la palabra la suma al contador
    else:
        palabras_cantidad[i] = 1 # si es la primera vez o unica que encuentra la palabra asigna 1 
print("")
print(f"recuento : {palabras_cantidad}\n") #muestro el recuento en pantalla

# Ejercicio 6

alumnos = {} #inicializo diccionario

for x in range(3): #hago que el bucle pida 3 alumnos
    alumno = input("Ingrese el nombre del alumno :") #pido valor str
    nota_alumno_uno = float(input("Ingrese la primer nota :")) #pido las notas
    nota_alumno_dos = float(input("Ingrese la segunda nota :"))
    nota_alumno_tres = float(input("Ingrese la tercer nota :"))
    print("")
    #diccionario alumnos, le asigno nombre alumno, y cada una de sus notas
    alumnos[alumno]=nota_alumno_uno, nota_alumno_dos, nota_alumno_tres
print("")
for alumno, nota in alumnos.items(): #por cada alumno y sus notas en el diccionario alumnnos
    promedio = sum(nota) / len(nota) 
    #saco el promedio sumando las notas con la función "sum" y divido por cantidad de notas
    print(f"El promedio de {alumno} es {round(promedio,1)}")
    #muestro en pantalla el promedio y uso round para un número mas coherente

# Ejercicio 7

#inicializo los 2 set
parcial_uno = {2,7,8,10}
parcial_dos = {7,4,10,6}

print(("\nAprobó los dos"), parcial_uno & parcial_dos) #uso intersección, solo si aparecen en ambos va a sumarse
print(("Aprobaron uno"), parcial_uno ^ parcial_dos) #uso ^, solo si aprobo 1 solo de los 2 va a aparecer
print(("Aprobó al menos uno"), parcial_uno | parcial_dos) #uso |, si aprobo cualquiera de los 2 va a aparecer

# Ejercicio 8

stock = {"leche" : 5, "galletitas" : 10, "manzana" : 7} #le pongo valores iniciales
print("")
producto = input("Ingrese nombre del producto a consultar : ") #pido valor

if producto in stock:#si el valor ingresado esta dentro del diccionario "stock"
    print(f"\nSe encontraron {stock[producto]} unidades del producto {producto}")#muestro en pantalla cantidad
    print("")
    agregar_unidades = int(input("Ingrese la cantidad de unidades que desea agregar: "))#doy la opción de agregar cantidad a el stock
    stock[producto] += agregar_unidades #en la posición del producto seleccionado sumo el valor ingresado 
    print(stock) #muestro el stock actualizado
else:
    nuevo_producto = int(input(f"No se encontró {producto} en el stock, Ingrese el stock inicial :")) #si no encuentra el producto da la opción de agregarlo
    stock[producto] = nuevo_producto #agrego el producto a el diccionario
    print(stock)

# Ejercicio 9

#creo una agenda base
agenda = {
    ("Lunes", "10:00") : "Reunión",
    ("Martes", "13:00") : "Clase de Inglés",
    ("Miercoles", "15:00") : "Clase de Matematcas",
    ("Jueves", "12:00") : "Clase de Ciencias",
    ("Viernes", "17:00") : "Festejo",
}
print("")
dia = (input("Ingrese el dia a consultar : ")).capitalize() #uso capitalize para evitar errores
hora = input("Ingrese la hora (hh:mm) : ") #pido hora 
print("")
if (dia,hora) in agenda:#si tanto dia como hora estan en el diccionario agenda
    print(f"Ese día a esa hora la actividad es : {agenda[dia,hora]}\n") #muestro en pantalla el evento correspondiente
else:
    print("No hay evento")

# Ejercicio 10

#pongo un diccionario base como ejemplo
original = {"Argentina" : "Buenos aires", "Chile" : "Santiago"}
print("El diccionario original es :")
print(original)
print("")
# "for pais,capital in original.items() recorre todos los valores dentro de original"
invertido = {capital : pais for pais, capital in original.items()}
# "capital : pais" invierte la posición de el pais y la capital
print("El diccionario invertido es :")
print(invertido)
#muestro en pantalla el nuevo diccionario con los valores invertidos