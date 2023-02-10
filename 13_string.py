text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''

size = len(text)
print("El tamaño de: ", text, ". Es :", size)

print("El mensaje es: ", text)
print("Mensaje en mayúscula: ", text.upper())
print("Mensaje minúscula: ", text.lower())
print("Contar la letra a en el mensaje es:  ", text.count('a'))

print("Invierte las minúsculas o mayúsculas del mensaje original: ", text.swapcase())
print("El mensaje original inicia con 'Ella': ",text.startswith('Ella'))
print("El mensaje original termina con 'Rust': ",text.endswith('Rust'))
print("Reemplaza la palabra 'Python' por 'Go' en el mensaje original: ",text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2,". Es un digito? " ,text_2.isdigit())
print("'398' es un digito? ","398".isdigit())