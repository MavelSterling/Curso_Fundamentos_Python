# En este desafío, tienes una variable llamada number como string, 
# tu reto es determinar si ese string es un número par o impar. 
# Para hacer esta validación, debes transformar el string a number y 
# luego realizar una condicional que compruebe si el número es divisible por dos. 
# Si lo es, significa que el número es par y debes imprimir el mensaje Es par.
# Si no lo es, significa que el número es impar y debes imprimir el mensaje Es impar.


number = '10'
print(number)

# Escribe tu solución 👇
number = int(number)
if number % 2 == 0:
  print("Es par")
else:
  print("Es impar")