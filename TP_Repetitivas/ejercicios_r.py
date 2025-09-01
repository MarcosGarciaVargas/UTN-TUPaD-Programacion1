import random #importo modulo random

#Ejercicio 1 

for i in range(101):#cada numero en el rango 0 - 101 muestro en pantalla(excluye al 101)
    print(i)
print(" ")

#Ejercicio 2

numero_usuario = int(input("Ingrese un número entero:"))#le pido un int al usuario
digitos_num = 0 #contador

while numero_usuario > 0:#mientras el número ingresado sea mayor a 0
    numero_usuario = numero_usuario // 10 #le voy restando digitos de a 1
    digitos_num += 1 #los sumo en el contador

print (f"El número ingresado tiene {digitos_num} digitos")
print(" ")

#Ejercicio 3 

numero_1 = int(input("Ingrese el primer Número :"))#pido valores iniciales
numero_2 = int(input("Ingrese el segundo Número :"))

valor_final_suma = 0 #inicializo variable 

if numero_1 > numero_2:#si el primer numero es mas grande
    for i in (range(numero_2 + 1, numero_1)):#uso + 1 para no incluir numero 2
        valor_final_suma += i
elif numero_2 > numero_1:#si el segundo es mas grande es el orden contrario
    for i in (range(numero_1 + 1, numero_2 )):
       valor_final_suma += i

print (f"La suma de los valores entre estos dos numeros es :{valor_final_suma}")
print(" ")

#Ejercicio 4 

numero_final = 0 #inicializo variable
numero_bucle = int(input("Ingrese un Número :"))#pido un input

while numero_bucle != 0:#mientras el numero ingresado sea distinto a 0
    numero_final += numero_bucle #sumo los numeros en la variable del inicio
    numero_bucle = int(input("Ingrese un Número :")) #sigo el bucle

print(f"El total acumulado es {numero_final}")
print(" ")

#Ejercicio 5

numero_aleatorio = random.randint(0,9) #uso función randint
contador = 0 

numero_del_usuario = int(input('Ingrese un numero entre "0 y 9" :'))

while numero_aleatorio != numero_del_usuario:#mientras el numero aleatorio sea distinto al ingresado
    contador += 1 #sumo un intento
    numero_del_usuario= int(input("Ingrese otro numero :"))
else:
    contador += 1 # le sumo + 1 para que se vea la cantidad correcta de intentos
    print(f"Acertaste!, fueron necesarios {contador} intentos.")
print(" ")

#Ejercicio 6

for valor in range(100,-2, -2):#desde 100 hasta 0 restando de a 2
        print(valor)
print(" ")

#ejercicio 7

numero_user = int(input("Ingrese un número :"))
resultado_acumulacion = 0

for i in range (0,numero_user+1):
    resultado_acumulacion += i

print(f"La suma de los numeros entre 0 y {numero_user} es {resultado_acumulacion}")
print(" ")

#Ejercicio 8

numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0
numeros_restantes = 100 #lo uso de contador

while numeros_restantes > 0:
    numeros_restantes -= 1
    numero_a_evaluar = int(input("Ingrese un numero Entero: "))

    if numero_a_evaluar >= 0 and numero_a_evaluar % 2 == 0:
        numeros_positivos += 1
        numeros_pares += 1

    elif numero_a_evaluar < 0 and numero_a_evaluar % 2 == 0:
        numeros_negativos += 1
        numeros_pares += 1

    elif numero_a_evaluar >= 0 and numero_a_evaluar % 2 != 0:
        numeros_positivos += 1
        numeros_impares += 1

    else:
        numeros_negativos += 1
        numeros_impares +=1

#disculpas por la complejidad innecesaria del código
#me di cuenta luego de terminar que utilizando unicamente 2 "if" hubiera quedado mas prolijo 

print(f"La cantidad de Números Pares es {numeros_pares}")
print(f"La cantidad de Números Impares es {numeros_impares}")
print(f"La cantidad de Números Positivos es {numeros_positivos}")
print(f"La cantidad de Números Negativos es {numeros_negativos}")
print(" ")

#Ejercicio 9

numeros_a_sumar = 100 #contador
valor_total = 0

while numeros_a_sumar > 0: #va a seguir el bucle hasta llegar a 0
    numeros_a_sumar -= 1 #le resto al contador
    numero_para_media = int(input("Ingrese un número entero :"))
    valor_total += numero_para_media #voy sumando todos los numeros en una variable

media = valor_total / 100 #divido la suma por la cantidad de numeros

print(f"La media de estos valores es {media}")
print(" ")

#Ejercicio 10

numero_invertir = int(input("Ingrese un número entero: "))
numero_invertido = 0 #es la variable en la que se pasa el numero invertido

while numero_invertir > 0:
    digitos = numero_invertir % 10 #el resto que queda es siempre el ultimo número
    numero_invertido = numero_invertido * 10 + digitos #a la variable final le voy sumando los digitos en orden
    numero_invertir = numero_invertir // 10 #// división entera de el numero inicial(sirve para quitar el ultimo digito)

print(f"El numero invertido es {numero_invertido}")


