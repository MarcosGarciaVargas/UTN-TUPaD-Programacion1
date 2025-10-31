# Ejercicio 1 

def factorial_recursiva(x):
    if x == 0: #caso base, factorial de 0 1
        return 1
    else:
        return x * factorial_recursiva(x - 1) #uso formula factorial
    
numero_usuario = int(input("Ingrese un número entero positivo: "))#le pido un valor al usuario

for i in range(1, numero_usuario + 1): #hago iteracion desde 1 hasta el ultimo numero
    print(f"\nla factorial del número {i} es {factorial_recursiva(i)} ")

# Ejercicio 2 

def fibonacci_recursiva(posicion):
    if posicion == 0: #ingreso los primeros 2 números de la serie 
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursiva(posicion - 1) + fibonacci_recursiva(posicion - 2) #sumo los 2 numeros anteriores
    

posicion_usuario = int(input("\nIngrese una posición: "))
for x in range(posicion_usuario + 1):
    print(f"el valor en la posición {x} es {fibonacci_recursiva(x)}") #muestro en pantalla

# Ejercicio 3

def potencia_num(base, exponente):
    if exponente == 0: #numero elevado a la 0 es 1
        return 1
    else:
        return base*potencia_num(base, exponente - 1)
    
base_usuario = int(input("\nIngrese un número base : ")) #le pido al usuario valores
exponente_usuario = int(input("Ingrese un exponente de ese número : "))
print(f"\nsi elevamos {base_usuario} por {exponente_usuario} el resultado es {potencia_num(base_usuario, exponente_usuario)}")

# Ejercicio 4

def pasar_a_binario(num):
    if num == 0: #caso base 
        return "0"
    else:
        return pasar_a_binario(num // 2) + str(num%2) 
    #divido el numero por 2 y concatena los 0 - 1 como string de atras hacia adelante
numero_decimal = int(input("\nIngrese un número entero positivo : "))
numero_binario = pasar_a_binario(numero_decimal)
print(f"\nEl numero {numero_decimal} en binario es {numero_binario}")#muestro en pantalla

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1: #caso base si la palabra esta vacia o es una sola letra
        return True
    elif palabra[0] != palabra[-1]: #si ambos lados no coinciden no cumple
        return False
    else:                   #con el 1:-1 quitamos extremos y verificamos simetria
        return es_palindromo(palabra[1:-1])
    
palabra_usuario = input("\nIngrese una palabra sin espacios ni tildes : ").lower()
print(f"\n{es_palindromo(palabra_usuario)}")

# Ejercicio 6

def suma_digitos(n):
    if n < 10: #caso base q1 solo digito
        return n
    else:
        return (n % 10) + suma_digitos(n // 10) #suma el último digito y va llamando recursivamente
    
numero_usuario = int(input("\nIngrese un numero entero positivo : "))
print(f"La suma de los digitos de {numero_usuario} da como resultado {suma_digitos(numero_usuario)}")

# Ejercicio 7

def contar_bloques(n):
    if n == 0:
        return 0 
    else:#sumo bloques actuales y los de nivel superior
        return n + contar_bloques(n-1)
    
bloques_piramide = int(input("\nIngrese la cantidad de bloques en el nivel mas bajo : "))
print(f"El total de bloques necesarios para construir la piramide es {contar_bloques(bloques_piramide)}")

# Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito: #si el ultimo digito es igual suma 1
        return 1 + contar_digito(numero // 10, digito)
    else:#si no coincide sigue con los otros
        return contar_digito(numero // 10, digito)
    
numero_contar = int(input("\nIngrese un número entero positivo : "))
digito = int(input("Dígito a contar (0 - 9): "))

print(f"\nEl digito {digito} aparece {contar_digito(numero_contar, digito)} veces en el numero {numero_contar}")



