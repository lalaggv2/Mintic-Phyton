#Entrada

nota1 = float(input('Ingrese nota 1: '))
nota2 = float(input('Ingrese nota 2: '))
nota3 = float(input('Ingrese nota 3: ')) 

#Proceso

definitiva = (nota1 * 0.3) + (nota2 * 0.3) + (nota3* 0.4)

#Salida
print('\nNota Definita: ', definitiva)

"""
Programa que permite calcular la nota definitiva de una materia, apartir de las tres notas
la primera nota vale el 30%
la segunda nota vale el 30%
la tecera nota vale el 40%
"""

# Entrada
nota1 =   float(input('Ingrese nota 1: '))
nota2 =   float(input('Ingrese nota 2: '))
nota3 =   float(input('Ingrese nota 3: '))

#Proceso

definitiva = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)


#Salida
print('\nNota Defintiva: ',definitiva)

# Así se hacen los comentarios 

nombre = "Miguel" # variable tipo texto con comillas dobles
apellido = 'Hernández' # variable tipo texto con comilla sencilla 
# se puede utilizar comillas simples o dobles  
# Lo recomendable es hacer comentarios, que ayudan a un mejor entendimiento del programa
#en lo posible los nombres de las variables debe indicar que dato almacenara

print ("¡Hola mundo!, bienvenido", nombre, apellido, "este es su primer programa")

"""
     Este progra permite realizar las operaciones de suma, resta, multipicación y división
     haciendo usos de los operadores + - * /
     input: función que permite la lectura de datos
     print: función que permite la impresión en pantalla de datos, texto, etc.
     int: tipo de dato numérico entero
"""

x = int(input('Digite un número '))
y = int(input('Digite un número '))
suma =  x + y
resta = x - y
producto = x * y
division = x / y
print(suma)
print(resta)
print(producto)
print(division)

# Elaborar un programa en Python que a partir de tres números ingresados por teclados calcule el promedio.

x = int( input ( 'Digite el primer número '))
y = int( input ( 'Digite el segundo número '))
z = int( input ( 'Digite el tercer número '))
promedio = (x + y + z)/3
print ('promedio ',promedio)

"""
     Este programa que utiliza los operadores relaciones > >= < <= == !=
"""

#Operadores de igualdad
a = 7
b = 9
#Operadores Relacionales
#== devuelve verdadero si dos valores son iguales
print(a == b)
#!= devuelve verdadero si dos valores son diferentes
print(a != b)
#> mayor que, devuelve verdadero si el primero operador 
# es estrictamente mayor que el segundo operador
print(a > b)
#< menor que, devuelve verdadero si el primero operador es 
# estrictamente menor que el segundo operador
print(a < b)
#>= mayor o igual
print(a >= b)
#<= menor o igual
print(a <= b)

#Operadores lógicos
a = True
b = False
#not: negación: not(var)
print(not(a))
#and: conjunción: var1 and var2
print(a and b)
#or: disyunción: var1 or var2
print(a or b)

edad = int(input(('Digite la edad: ')))
if edad > 18:
    print('Puede ejercer el libre derecho al voto')
else:
    print('No puede votar...')

print(" Digite dos números: ")
n1=int(input(" Número 1: "))
n2=int(input(" Número 2: "))

print("\n MENÚ \n Digite el número correspondiente a la operación que quiera realizar:")
print("\n\t1. Suma de los dos números")
print("\t2. Resta de los dos números")
print("\t3. Multiplicación de los dos números")

opcion=int(input("\n Digite la operacion a realizar: "))
if opcion ==1:
  print(" El resultado de la suma de ",n1,"+", n2, "=", n1+n2)
elif opcion ==2:
  print(" El resultado de la resta de ",n1,"-", n2, "=", n1-n2)
elif opcion ==3:
  print(" El resultado de la multiplicación de ",n1,"x", n2, "=", n1*n2)
else:
  print(" Opcion errada ")
