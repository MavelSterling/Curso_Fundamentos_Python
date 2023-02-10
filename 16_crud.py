# CRUD Create, Read, Update & Delete

numbers = [1, 2 , 3 , 4 , 5]
print(numbers[1]) # posicion 2
numbers[-1] = 10 # Agregar elemento al final de la lista
print(numbers)

numbers.append(700) # Agregar elemento al final de la listas
print(numbers)

numbers.insert(0, 'hola') # Agregar elementos en la posicion 0 de la lista
print(numbers)

numbers.insert(3, 'change') # Agregar elementos en la posicion 4 de la lista
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3'] # Crear lista
new_list = numbers + tasks # Unir la lista numbers con tasks
print(new_list)

index = new_list.index('todo 2') # indice del elemento 'todo 2'
new_list[index] = 'todo changed' # Se cambia el elemento 'todo 2' por el elemento 'todo changed'
print(new_list)

new_list.remove('todo 1') # Remover el elemento 'todo 1'
print(new_list)

new_list.pop() # Remueve el último elemento de la lista
print(new_list)

new_list.pop(0) # Remueve el elemento de la posicion 0 de la lista
print(new_list)

new_list.reverse() # Invierte el orden de la lista - Inicia por el final de la lista
print(new_list)

numbers_a = [1, 4, 6 , 3] # Crear lista
numbers_a.sort() # Orderar el lista de menor a mayor
print(numbers_a)

strings = ['re', 'ab', 'ed'] # Crear lista
strings.sort() # Orderar el lista por el alfabeto
print(strings)

# no se ordenar listas con datos mezclados : string, numbers