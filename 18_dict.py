# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

my_dict = {}
print("El tipo de la variable my_dict es: ",type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print("El diccionario es: ",my_dict)
print("La cantidad items en el diccionario es: " ,len(my_dict))

print("La edad almacena en el diccionario es: " , my_dict['age'])
print("El apellido almacena en el diccionario es: " + my_dict['last_name'])


#La funcion get, si no existe el valor sale un mensaje none(Maneja el error)
# Se cambian los corchetes por parentesis(), ya que get es una funcion de python
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)