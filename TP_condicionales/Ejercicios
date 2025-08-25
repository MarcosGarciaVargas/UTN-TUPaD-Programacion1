from statistics import mode,median, mean
import random

#Ejercicio 1 

edad_usuario = int(input("Ingrese su edad: "))#le pido al usuario que ingrese su edad

if edad_usuario >= 18:#si la edad es mayor o igual a 18
    print("Es mayor de edad")
print(" ")

#Ejercicio 2 

nota_usuario = int(input("Ingrese su nota: "))#le pido al usuario que ingrese valor

if nota_usuario >= 6:#si el valor es mayor o igual a 6
    print("Aprobado")#muestro en consola
else:#si no se da el caso anterior
    print("Desaprobado")#muestro en consola
print(" ")

#Ejercicio 3 

numero_par_impar = int(input("Ingrese un numero: "))#pido un valor
resto = numero_par_impar % 2 #saco el resto del numero ingresado

if resto == 0:#si el resto es cero significa que es par
    print("El numero es par")
else:#de lo contrario es un numero impar
    print("Por favor, ingrese un numero par")
print(" ")

#Ejercicio 4

grupo_edad = int(input("Ingrese su edad: "))#pido un valor

if grupo_edad < 12:#si el valor edad es menor a 12 se muestra el siguiente mensaje
    print("Usted es un niño")
elif grupo_edad < 18:#si la edad es mayor a 12 y menor a 18
    print("Usted es un adolescente")
elif grupo_edad < 30:#si la edad es igual o mayor a 18 y menor que 30
    print("Usted es un adulto joven")
else:#si la edad es mayor o igual a 30
    print("Usted es un adulto")
print(" ")

#Ejercicio 5 

contraseña_usuario = (input("Ingrese su contraseña: "))#pido un valor

longitud_contraseña = (len(contraseña_usuario))#uso la función "len" para calcular la longitud

if longitud_contraseña >= 8 and longitud_contraseña <= 14:#si la longitud es igual o mayor a 8 y menor o igual a 14
    print("Ha ingresado una contraseña correcta")
else:#de caso contrario osea menor a 8 o mayor a 14
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print(" ")

#Ejercicio 6

numeros_aleatorios = [random.randint(1,100) for i in range(50)]#uso el modulo random para aleatorizar los numeros

moda = mode(numeros_aleatorios)#uso la función mode en "numeros_aleatorios"
mediana = median(numeros_aleatorios)#uso la función median en "numeros_aleatorios"
media = mean(numeros_aleatorios)#uso la función mean en "numeros_aleatorios"

#print("Numeros aleatorios :",numeros_aleatorios) ocupa mucho lugar en la consola, no se si era necesario mostrarlo
print("Moda :",moda)#muestro en pantalla los 3 resultados
print("mediana :",mediana)
print("media :",media)

if media > mediana and mediana > moda:#si media es mayor a mediana y mediana mayor a moda
    print("sesgo positivo")
elif media < mediana and mediana < moda:#si media es menor a mediana y mediana menor a moda
    print("sesgo negativo")
elif media == mediana == moda:#si las 3 son iguales
    print("sin sesgo")
else:#si no se da ninguno de los 3 casos
    print("Distribución no cumple con los criterios")

print(" ")

#Ejercicio 7

palabra_usuario = (input("Ingrese una palabra: "))#pido un valor

ultima_letra = palabra_usuario[-1].lower()#tomo la ultima letra del string con [-1] y paso la variable a lowercase con lower()

if(ultima_letra == "a" or
   ultima_letra == "e" or
   ultima_letra == "i" or
   ultima_letra == "o" or
   ultima_letra == "u"):

   print(f"{palabra_usuario}{"!"}")#muestro el print con ! en caso de que la palabra termine en vocal
else:
    print(palabra_usuario)
print(" ")

#Ejercicio 8

nombre_usuario = input("Ingrese su nombre: ")#pido el nombre
print("Ingrese el numero [1] si quiere su nombre en Mayusculas")
print("Ingrese el numero [2] si quiere su nombre en Minusculas")
print("Ingrese el numero [3] si quiere SOLO la primer letra Mayuscula")
numero_usuario = int(input("Numero: "))#pido que ingrese numero del 1-3

if numero_usuario == 1:#si numero es igual a 1
    nombre_upper = (nombre_usuario).upper()#paso el string a uppercase
    print(nombre_upper)
elif numero_usuario == 2:#si numero es igual a 2
    nombre_lower = (nombre_usuario).lower()#paso el string a lowercase
    print(nombre_lower)
elif numero_usuario == 3:#si numero es igual a 3
    nombre_title = (nombre_usuario).title()#capitalizo la primer letra 
    print(nombre_title)
else:#en caso de que el valor no sea 1,2 o 3
    print("valor incorrecto")
print(" ")

#Ejercicio 9

magnitud_terremoto = int(input("Ingrese la magnitud del terremoto: "))#pido el valor del terremoto y lo paso a int

if magnitud_terremoto < 3:#si la magnitud es menor a 3
    print("Muy leve (imperceptible)")
elif magnitud_terremoto < 4:#si la magnitud es menor a 4 
    print( "Leve (ligeramente perceptible)")
elif magnitud_terremoto < 5: #si la magnitud es menor a 5 
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
print(" ")

#ejercicio 10

hemisferio = input("Ingrese su hemisferio (Norte|Sur): ").lower()#pido que ingrese su hemisferio y lo paso a lowercase para evitar errores
mes = int(input("Ingrese su mes (1-12):"))
dia = int(input("Ingrese su dia:"))

if hemisferio == "norte":
    if (mes == 12 and dia >=21) or (mes == 1 or mes == 2) or (mes == 3 and dia <=20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <=20):
        estacion = "Primavera"
    elif (mes == 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <=20):
        estacion = "Verano"
    elif (mes == 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"

elif hemisferio == "sur":
    if (mes == 12 and dia >=21) or (mes == 1 or mes == 2) or (mes == 3 and dia <=20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <=20):
        estacion = "Otoño"
    elif (mes == 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <=20):
        estacion = "Invierno"
    elif (mes == 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"

print(f"Usted se encuentra en {estacion}")
