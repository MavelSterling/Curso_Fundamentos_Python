lives = 3
print(type(lives))

age = 12
buget = 100


temperature=12.12
print(type(temperature))

lives = 2
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

# disminuye 1
lives -= 1
print(lives)

# disminuye 5
lives -= 5
print("disminuye 5",lives)

# incrementa 5
lives += 5
print("Incrementa 5",lives)

number = 4500000000000000000.1
print(number)

number_b = 0.0000000000000001
print(number_b)


gasto1 = input("Dígita el valor primer gasto: ")
gasto2 = input("Dígita el valor segundo gasto: ")
gasto3 = input("Dígita el valor tercer gasto: ")

gastos = [gasto1,gasto2,gasto3]

promedio = round(((int(gasto1) + int(gasto2) + int(gasto3)) / len(gastos)),2)
print(f'El promedio de los gastos en un mes es: {promedio}')