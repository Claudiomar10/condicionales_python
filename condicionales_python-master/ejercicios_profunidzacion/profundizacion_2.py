# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Objetizo:
Realizar un programa que solicite ingresar
tres valores decimales de temperatura
De las temperaturas ingresadas se determinará:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.

Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la mayor temperatura. Deberá almacenar
el valor de la temperatura más alta en una nueva variable
llamada:
--> temperatura_max

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la menor temperatura. Deberá almacenar
el valor de la temperatura más baja en una nueva variable
llamada:
--> temperatura_min

- Al final imprimir en pantalla la variable temperatura_max
  y temperatura_min
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input('Ingrese Primer Valor de Temperatura: \n'))
temperatura_2 = float(input('Ingrese Segundo Valor de Temperatura: \n'))
temperatura_3 = float(input('Ingrese Tercer Valor de Temperatura: \n'))

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
  print (f'La Temperatura Maxima es la Primer Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 == temperatura_2 and temperatura_1 > temperatura_3:
  print(f'Las Temperaturas Máximas son la Primer y Segunda Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 > temperatura_2 and temperatura_1 == temperatura_3:
  print(f'Las Temperaturas Máximas son la Primer y Tercer Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 == temperatura_2 and temperatura_1 == temperatura_3:
  print(f'Las Tres Temperaturas ingresadas son iguales y Maximas: {temperatura_1} grados')

elif temperatura_2 > temperatura_3:
  print(f'La Temperatura Máxima es la Segunda Temperatura ingresada: {temperatura_2} grados')
elif temperatura_2 == temperatura_3:
  print(f'Las Temperaturas Máximas son la Segunda y la Tercer Temperatura ingresada: {temperatura_2} grados')
  
else:
  print(f'La Temperatura Maxima es la Tercer Temperatura ingresada: {temperatura_3} grados')
  
#TEMPERATURA MINIMA
if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
  print (f'La Temperatura Minima es la Primer Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 == temperatura_2 and temperatura_1 < temperatura_3:
  print(f'Las Temperaturas Minimas son la Primer y Segunda Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 < temperatura_2 and temperatura_1 == temperatura_3:
  print(f'Las Temperaturas Minimas son la Primer y Tercer Temperatura ingresada: {temperatura_1} grados')
elif temperatura_1 == temperatura_2 and temperatura_1 == temperatura_3:
  print(f'Las Tres Temperaturas ingresadas son iguales y Minimas: {temperatura_1} grados',)

elif temperatura_2 < temperatura_3:
  print(f'La Temperatura Minima es la Segunda Temperatura ingresada: {temperatura_2} grados')
elif temperatura_2 == temperatura_3:
  print(f'Las Temperaturas Minimas son la Segunda y la Tercer Temperatura ingresada: {temperatura_2} grados')
  
else:
  print(f'La Temperatura Minima es la Tercer Temperatura ingresada: {temperatura_3} grados')