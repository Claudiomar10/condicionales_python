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
¡Realizar un juego de trivia!
Usted cuenta con la variables "preguntas" y "respuestas",
por cada pregunta se debe consultar al usuario que juega
cuál es la respuesta correcta.

Cada respuesta correcta otorga 10 puntos.

Importante: Ingresar los nombres sin tildes.

Alumno:
- Crear una variable llamada puntaje inicializada,
  en cero. Esta variable la deberá incrementar en 10
  por cada respuesta correcta.

- Deberá imprimir en consola una pregunta por vez,
  y con la función input en cada caso solicitar una respuesta
  por cada pregunta realizada.

- Utilizar condicionales para evaluar si la respuesta
  ingresada por el usuario coincide con la respuesta
  del programa (las variables).

- Cada respuesta ingresada por el usuario por consola
  la deberá pasar a minúsculas utilizando la función
  lower (cómo se vio los ejemplos de clase)

- Imprimir al final del programa el puntaje total
'''

print('Juego de trivia')
puntaje = 0

pregunta_1 = "¿Cuál es la capital de Argentina?"
respuesta_1 = "buenos aires"

pregunta_2 = "¿Cuál es la capital de Perú?"
respuesta_2 = "lima"

pregunta_3 = "¿Cuál es la capital de Uruguay?"
respuesta_3 = "montevideo"

pregunta_4 = "¿Cuál es la capital de Colombia?"
respuesta_4 = "bogota"

pregunta_5 = "¿Cuál es la capital de Venezuela?"
respuesta_5 = "caracas"

# Empezar aquí la resolución del ejercicio
print('Juego de Preguntas y Respuestas')
print ('¿Cuál es la capital de Argentina?')
respuesta_11 = input('Ingrese su respuesta:\n')
print()
if respuesta_1 == respuesta_11.lower():
  print('Respuesta Correcta')
  puntaje +=10
else:
  print('Respuesta Incorrecta')
print()
print('¿Cuál es la capital de Perú?')
respuesta_22 = input('Ingrese su respuesta:\n')
print()
if respuesta_2 == respuesta_22.lower():
  print('Correcto')
  puntaje +=10
else:
  print('Respuesta Incorrecta')
print()
print('¿Cuál es la capital de Uruguay?')
respuesta_33 = input('Ingrese su respuesta:\n')
print()
if respuesta_3 == respuesta_33.lower():
  print('Correcto')
  puntaje +=10
else:
  print('Respuesta Incorrecta')
print()
print('¿Cuál es la capital de Colombia?')
respuesta_44 = input('Ingrese su respuesta:\n')
print()
if respuesta_4 == respuesta_44.lower():
  print('Correcto')
  puntaje +=10
else:
  print('Respuesta Incorrecta')
print()
print('Cuál es la capital de Venezuela?')
respuesta_55 = input('Ingrese su respuesta:\n')
print()
if respuesta_5 == respuesta_55.lower():
  print('Correcto')
  puntaje +=10
else:
  print('Respuesta Incorrecta')
print()
print(f'El puntaje final obtenido es: {puntaje} puntos')