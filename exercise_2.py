# En este desafío, se te proporcionará una lista de letras llamada letters. 
# Tu reto es realizar las siguientes operaciones en orden:

# 1. Agregar la letra G al final de la lista.
# 2. Reemplazar la letra en la posición 0 con la letra Z.
# 3. Eliminar la letra C de la lista.
# 4. Imprimir la lista resultante al revés.

letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)