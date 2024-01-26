# -*- coding: utf-8 -*-

# comentario

saludo = "Hola!"

print(saludo)

# ciclo for

a = 0 # Se define la variable

for i in range(5):
    a+=1 # aumenta de 1
    print(a)
    
    
# Operadores

print(5+6)
print(6-5)
print(5*6)
print(5/6)

# Modulo: el resto de una división

print(10%3)

# Exponente

print(5**3)

print(9//2)

# Variable

numero =5

print("La variable numero es: ",numero)

print(type(numero)) # tipo entero 'int'

nombre = "ML"

print(type(nombre)) # tipo string 'str'

numero1 = 5.2

print(type(numero1)) # tipo flotante 'float'

mensaje = """ Esto es un mensaje
... con tres saltos
... de línea"""

print(mensaje)

numero_1 = 5
numero_2 = 7
if numero_1>numero_2:
    print("El numero1 es mayor", numero_1)
else:
    print("El numero 2 es mayor", numero_2)