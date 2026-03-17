# PRIMERA PRACTICA DE PYTHON
print("Hola mundo desde Python !!! ")

# Variables en Python

# Enteros
edad = 20
# float
precio = 50.5
# string
nombre = "Bruno Diaz"
# boolean
bandera = True

#Salida de datos
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Precio: ", str(precio))

# Entrada de datos
nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

#SEGUNDA PRACTICA DE PYTHON
#Entrada de datos
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2

print("La suma es: ", suma)

num3 = float(input("Ingrese el primer numero: "))
num4 = float(input("Ingrese el segundo numero: "))

suma_f = num3 + num4

print("La suma es: ", suma_f)

#TERCERA PRACTICA DE PYTHON

# Metodos 
curso = "Python para principiantes"
print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.capitalize())

# Busquedas
print(curso.find("h"))
print(curso.find("cia"))

# Replazos
print(curso.replace("para", "FOR"))
print(curso)

# Operadores logicos
print ("PARA" in curso)

#CUARTA PRACTICA DE PYTHON
# Operadores matematicos

print(10 + 5) # Suma
print(10 - 5) # Resta
print(10 * 5) # Multiplicacion
print(10 / 4) # Division


print(10 // 4) # Division entera

print(10 % 3) # Modulo - rresiduo

print(2 ** 4) # Potencia - exponente

x = 10
x = x +5
print (x)
# Operador de asignacion compuesto
y = 20
y += 5 
y *=5
print (y)
# Precedencia de operadores
x = 10 + (3 * 2)
print(x)

#QUINTA PRACTICA DE PYTHON
#Expresiones booleanas
x = 3 > 2
print(x)

x = 5 == 3
print(x)

x = 5 != 3
print(x)

# Operadores logicos And or, not
precio = 25
print(precio > 20 and precio < 30) # AND
precio = 5
print(precio > 20 or precio < 30) # OR  
print(not (precio > 10)) # NOT


print(10 > 5) # Mayor que
print(10 < 5) # Menor que
print(10 == 5) # Igual que
print(10 != 5) # Diferente de
print(10 >= 5) # Mayor o igual que
print(10 <= 5) # Menor o igual que

#SEXTA PRACTICA DE PYTHON
#Sentencia
temperatura = int(input("Ingrese la temperatura actual: "))

if temperatura > 28:
    print("Esta haciendo calor")
else:
    print("Esta haciendo frio")
    
if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Esta haciendo un poco de frio")
else:
    print("Esta haciendo frio, brrrr")

print("Fin del programa")

#SEPTIMA PRACTICA DE PYTHON
# Bucles
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1
    
i = 1
while (i >= 10):
    print(i * "#")
    i += 1

#OCTAVA PRACTICA DE PYTHON
# Listas
frutas = ["Manzana", "Fresa" , "Naranja", "Pera" , "Maracuya"]
print(frutas)
print(frutas[0]) # Acceder al primer elemento
print(frutas[2]) # Acceder al tercer elemento
print(frutas[-1]) # Acceder al ultimo elemento :)
print(len(frutas)) # Acceder a la longitud de la lista

# Agregar un elemento a la lista
frutas.append("Sandia")
print(frutas)
# Rango
print(frutas[1:4]) # Acceder a un rango de elementos

frutas.append("Kiwi") # Agregar un elemento al final de la lista

#NOVENA PRACTICA DE PYTHON
# Metodos de listas
numeros = [1,2,3,4,5]
# Agregar un elemento al final de la lista
numeros.append(6)
print(numeros)
# Insertar un elemento en una posicion especifica
numeros.insert(0, -1) 
print(numeros)
numeros.insert(1, 0) 
print(numeros)

#Eliminar un elemento de la lista
numeros.remove(3)
print(numeros)
# Eliminar el ultimo elemento de la lista
numeros.pop()
print(numeros)
#Tamaño de la lista
print(len(numeros))
#Verificar si un elemento esta en la lista
print(4 in numeros)
# Eliminar el contenido de la lista
numeros.clear()
print(numeros)

#DECIMA PRACTICA DE PYTHON
# Objeto range
numeros = range(5) # Crea un rango de numeros 
print(numeros)
print(list(numeros)) # Convertir el rango a una lista

for item in numeros:
    print(item)
    
for item in range(5, 10): # Rango con inicio, fin y paso
    print(item)
    
for item in range(10, 20, 2): # Rango con inicio, fin y paso
    print(item)
    
#ONCEAVA PRACTICA DE PYTHON
#Tuplas (inmutables)
tupla_numero = (1, 2, 3, 4, 5, 6)
print(tupla_numero)

print(tupla_numero[3]) # Acceder al primer elemento
print(tupla_numero.count(5)) # Contar cuántas veces aparece el número 5
print(tupla_numero.index(5)) # Obtener el índice del número 5
print(tupla_numero[-1]) # Acceder al ultimo elemento
print(len(tupla_numero)) # Acceder a la longitud de la tupla

#DOCEAVA PRACTICA DE PYTHON
# Diccionarios (key-value) Almacena a pares de clave-valor
mi_diccionario = { "nombre": "Bruno Diaz", "edad": 30, "ciudad": "Santiago"}
print(mi_diccionario)

# Acceder a los valores del diccionario
print(mi_diccionario["nombre"]) # Acceder al valor de la clave "nombre"
print(mi_diccionario["ciudad"]) # Acceder al valor de la clave "ciudad"
print(mi_diccionario["edad"]) # Acceder al valor de la clave "edad"

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)

# Eliminar un par clave-valor del diccionario
del mi_diccionario["ciudad"]
print(mi_diccionario)

# Obtener las claves del diccionario
print(mi_diccionario.keys())

# Obtener los valores del diccionario
print(mi_diccionario.values())

# Verificar si una clave existe en el diccionario
if 'edad' in mi_diccionario:
    print("Clave encontrada")

# Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("Clave: " ,clave," Valor: ",valor)

#TRECEAVA PRACTICA DE PYTHON
# Funciones - Son bloques de codigo reutque realiza una tarea especifica y que son reutilizables 
def saludar():
    print("Hola , bienvenido al curso de Python")

#Funciones con parametros
def saludo(nombre):
    print("Hola " + nombre + " bienvenido a clases")
    
# Funciones con valor de retorno
def sumar(a, b):
    return a + b

# Esablecer un valor por defecto para un parametro
def bienvenida(nombre = "Estudiante"):
    print("Bienvenido", nombre)

# Funciones con argumentos variables
def sumador(*args):
    return sum(args)

# Llamar a la funcion
saludar()
saludo("Diana Canaviri")

resultado = sumar(10, 4)
print("El resultado de la suma es:", resultado)

bienvenida()
bienvenida("Diana Canaviri")

print(sumador(1, 2, 3, 4, 5))
print(sumador(4, 5, 6))