#Ejercicio 1 

print ("Hola mundo")

#ejercicio 2 

nombre = input("Ingrese su nombre :")
print(" ")
print(f"Bienvenido " + nombre +"!")
print(" ")
#ejercicio 3

nombre = input("Ingrese su nombre :")
apellido = input("Ingrese su apellido :")
edad = input("Ingrese su edad :")
residencia = input("Ingrese su lugar de residencia:")
print(" ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
print(" ")

#ejercicio 4 

radio = input("Ingrese el radio de un círculo : ")

radio = (int(radio))

area = 3.14*radio**2

perimetro = 2*3.14*radio

print(f"El area de su círculo es : {area} y el perímetro : {perimetro}")
print(" ")
#ejercicio 5 

segundos = input("Ingrese una cantidad de segundos : ")

segundos = (int(segundos))

horas = segundos/3600
horas = (int(horas))


print(f"Esos segundos equivalen a {horas} hora(s)")
print(" ")

#ejercicio 6 

numero = input("Ingrese un numero : ")

numero = (int(numero))

print ("La tabla de multiplicar de este numero es :")
print (numero*1)
print (numero*2)
print (numero*3)
print (numero*4)
print (numero*5)
print (numero*6)
print (numero*7)
print (numero*8)
print (numero*9)
print (numero*10)

#no utilice un bucle "if" ya que no sabia si estaba permitido, pero era la forma que considero correcta 

print(" ")
#ejercicio 7 

numero_uno = input("Ingrese un numero entero distinto a 0 : ")

numero_dos = input("Ingrese otro numero entero distinto a 0 : ")

numero_uno = (int(numero_uno))
numero_dos = (int(numero_dos))

suma = (numero_uno + numero_dos)

resta = (numero_uno - numero_dos)

multiplicacion = (numero_uno * numero_dos)

division = (numero_uno / numero_dos)
print(" ")
print (f"La suma de estos numeros da como resultado : {suma}")
print (f"La resta de estos numeros da como resultado : {resta}")
print (f"La multiplicación de estos numeros da como resultado : {multiplicacion}")
print (f"La división de estos numeros da como resultado : {division}")
print(" ")

#ejercicio 8 

altura = input("Ingrese su altura en metros : ")

peso = input("Ingrese su peso en kg : ")

altura = float(altura)
peso = int(peso)


indice_corporal = peso/(altura**2)

print (f"Su indice de masa corporal es : {indice_corporal}")
print(" ")
#ejercicio 9 

grados_c = input("Ingrese una temperatura en celcius :")

grados_c = (float(grados_c))


fahrenheit = 9/5 * grados_c + 32

print (f"ese valor convertido a fahrenheit es : {fahrenheit}")
print(" ")
#ejercicio 10 

primer_numero = input("Ingrese su primer numero : ")
segundo_numero = input("Ingrese su segundo numero : ")
tercer_numero = input("Ingrese su tercer numero : ")

primer_numero = (int(primer_numero))
segundo_numero = (int(segundo_numero))
tercer_numero = (int(tercer_numero))

promedio = (primer_numero + segundo_numero + tercer_numero)/3

print (f"El promedio entre estos tres numeros es : {promedio}")