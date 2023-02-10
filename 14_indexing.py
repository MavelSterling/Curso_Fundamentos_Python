text = "Ella sabe Python"
print("Primera letra del mensaje: ",text[0])
print("Segunda letra del mensaje: ",text[1])


# print(text[999])
size = len(text)
print('size => ',size)
print("La última letra del mensaje: ", text[size - 1])
print("La última letra del mensaje: ",text[-1])

# slicing

print("Las 5 posiciones del mensaje: ", text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print("El mensaje original es: ",text[:])
print("La última palabra del mensaje: ", text[10:16:1])
print("La última palabra del mensaje con saltos de 2 letras: ",text[10:16:2])
print(text[::2])