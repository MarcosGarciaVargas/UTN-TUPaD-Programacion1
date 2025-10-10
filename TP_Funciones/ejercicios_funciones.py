# Ejercicio 1 
print("\n")
def imprimir_hola_mundo():
    print("Hola mundo!") #muestra mensaje en pantalla

imprimir_hola_mundo()#llamo a la función
print("\n")
# Ejercicio 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")#muestra el mensaje en pantalla y cambia en base a variable

nombre = input("Ingrese su nombre: ")#pido input
print("")
saludar_usuario(nombre)#llamo función y le asigno la variable
print("\n")
# Ejercicio 3 

def informacion_personal(nombre, apellido, edad, residencia):
    #muestro mensaje en pantalla con los valores
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#pido un input para cada caso
nombre_personal = input(f"Ingrese su nombre: ")
apellido_personal = input(f"Ingrese su apellido: ")
edad_personal = input(f"Ingrese su edad: ")

#si edad no esta vacío y es distinto a 0 y positivo
if not edad_personal.isdigit() or int(edad_personal) <= 0:
    print("Edad inválida")
else:
    residencia_personal = input(f"Ingrese su lugar de residencia: ")
    #llamo a la función con las 4 variables
    print("")
    informacion_personal(nombre_personal, apellido_personal, edad_personal, residencia_personal)
print("\n")
# Ejercicio 4

def calcular_area_circulo(radio):
    #calculo para sacar el area
    calcular_area = 3.14 * radio**2
    return calcular_area

def calcular_perimetro_circulo(radio):
        #calculo para sacar el perimetro
    calcular_perimetro = 2 * 3.14 * radio
    return calcular_perimetro
#pido un input de número
radio = float(input("Ingrese el radio del círculo :"))
print("\n")
if radio <= 0:#si el radio es 0 o negativo
    print("Radio incorrecto, ingrese otro valor")
else:
    #muestro mensaje en pantalla, uso round para dejar solo los primeros 2 decimales
    print(f"El area del círculo es : {round(calcular_area_circulo(radio),1)}")
    print(f"El perimetro del círculo es : {round(calcular_perimetro_circulo(radio),1)}")
print("\n")
# Ejercicio 5
#hago el calculo de segundos a horas
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
#pido valor y muestro en pantalla
segundos = int(input("Ingrese una cantidad de segundos :"))

if segundos < 0:#si segundos es negativo
    print("Los segundos deben ser positivos")
else:
    print(f"El equivalente de esos segundos en horas es :{round(segundos_a_horas(segundos),2)}")
print("\n")
# Ejercicio 6

def tabla_multiplicar(numero):
    #hago una iteración hasta que llegue a 10(11-1)
    for i in range(1, 11):
        #voy multiplicando por la i que aumenta en cada vuelta
        resultado = numero * i
        print(resultado)

#pido input y muestro en pantalla
numero_usuario = int(input("Ingrese un numero :"))
tabla_multiplicar(numero_usuario)
print("\n")
# Ejercicio 7

def operaciones_basicas_a(a, b):
    #hago todas las ecuaciones basicas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
#pido valores y los paso a float
a = float(input("Ingrese el primer Número :"))
b = float(input("Ingrese el segundo Número :"))
#invoco la función
cuentas = operaciones_basicas_a(a,b)
#indico la parte de la tupla en la que se encuentran los valores a mostrar
print("")
print(f"suma :{cuentas[0]}")
print(f"resta :{cuentas[1]}")
print(f"multiplicación :{cuentas[2]}")
print(f"División :{cuentas[3]}")
print("\n")
# Ejercicio 8

def calcular_imc(peso, altura):
    #calculo imc
    imc = peso / (altura**2)
    return imc
#pido input
peso = float(input("Ingrese su peso exacto en KG: "))
altura = float(input("Ingrese su altura en metros: "))
print("")
if peso <= 0 or altura <= 0:#validación basica, si peso o altura son menores o igual a 0, pide otro valor
    print("Ingrese un peso y edad correctos")
else:
    #muestro en pantalla y uso round
    print(f"Su IMC es : {round(calcular_imc(peso,altura),2)}")
print("\n")
# Ejercicio 9

def celsius_a_farenheit(celsius):
    #paso de celsius a farenheit
    paso_de_temperatura = (celsius * 9/5) + 32
    return paso_de_temperatura
#pido un valor y lo paso a float
celsius = float(input("Ingrese grados celsius :"))
print("")
#muestro en pantalla, uso round
print(f"Esos grados celsius pasado a farenheit es :{round(celsius_a_farenheit(celsius),2)}")
print("\n")
# Ejercicio 10

def calcular_promedio(a, b, c):
    #divido los 3 valores por 3
    promedio = (a + b + c)/3
    return promedio
#pido los inputs para asignar a cada variable
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print("")
#muestro mensaje por pantalla y uso round para mas visibilidad
print(f"El promedio de esos tres números es :{round(calcular_promedio(a,b,c),1)}")
print("")


