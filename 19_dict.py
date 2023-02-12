person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50 # Le dismimnuye 50 a la edad
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())

print("----------------------------------------------------------------")
Harry_potter={
    "name": "Harry Potter",
    "species": "human",
    "gender": "male",
    "house": "Gryffindor",
    "dateOfBirth": "31-07-1980",
    "yearOfBirth": 1980,
    "ancestry": "half-blood",
    "eyeColour": "green",
    "hairColour": "black",
    "wand": {
      "wood": "holly",
      "core": "phoenix feather",
      "length": 11
    },
    "patronus": ["stag",'Fox'],
    "hogwartsStudent": True,
    "hogwartsStaff": False,
    "actor": "Daniel Radcliffe",
    "alive": True,
    "image": "https://hp-api.herokuapp.com/images/harry.jpg"
  }

#Agregando un dato a un diccionario que esta en un diccionario ppal
print(Harry_potter['wand']['core'])
Harry_potter['wand']['core']+= ' dragon heartstring'
print(Harry_potter['wand']['core'])

#agregando un valor a una lista que esta en un diccionario ppal
print(Harry_potter['patronus'])
Harry_potter["patronus"].append('cat')
print(Harry_potter['patronus'])

#eliminar un par clave, valor de una lista que esta en un diccionario ppal
del Harry_potter["actor"]
Harry_potter.pop('gender')
print(Harry_potter)

#Obtener items de un diccionario
print('')
print('Items')
print(Harry_potter.items())

#Imprime las keys del diccionario
print('')
print('keys')
print(Harry_potter.keys())


#imprime las keys del diccionar que esta en un diccionar ppal
print('')
print('keys of dict in dict')
print(Harry_potter["wand"].keys())

#Imprime los values  del diccionario
print('')
print('values')
print(Harry_potter.values())


#imprime las keys del diccionar que esta en un diccionar ppal
print('')
print('values of dict in dict')
print(Harry_potter["wand"].values())