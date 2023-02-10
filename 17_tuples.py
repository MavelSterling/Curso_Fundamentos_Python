# Las tuplas se declaran con ()

numbers = (1, 2, 3, 5) # tuplas de números
strings = ('nico', 'zule', 'santi', 'nico') #tuplas de strings
print(numbers)
print('0 =>', numbers[0]) # Primer elemento de la tupla ---- acceder a los elementos de la tupla
print('-1 =>', numbers[-1]) # Último elemento de la tupla ---- acceder a los elementos de la tupla
print(type(numbers)) # El tipo de numbers

print(strings)
print(type(strings)) # El tipo de strings

# CRUD
# En las tuplas no se puede ser modificada elementos

# numbers.append(10) --- no tiene el método append
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule')) # Posicion de 'zule' en la tupla strings
print(strings.count('nico')) # Contar las veces se esta 'nico' en la tupla strings

my_list = list(strings) # Volver la tupla strings en una lista
print(my_list)
print(type(my_list)) # El tipo de my_list

my_list[1] = 'juli' # Se reemplaza el valor de la posición 1 de la lista 
print(my_list)

my_tuple = tuple(my_list) # Convertir la lista en tupla
print(my_tuple)