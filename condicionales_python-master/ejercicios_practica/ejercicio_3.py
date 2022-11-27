# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados elif

# Objetico
# Verificar la calificación de un estudiante según su
# puntaje en un examen
puntaje = 70

# Alumno:
# Deberá crear una serie de considiconales
# con if y elif de forma tal de cargar en
# la variable nota la nota del alumno según
# las siguientes condiciones:

nota = ""

# Si el puntaje es mayor igual a 90 --> nota = "A"
# Si el puntaje es mayor igual a 80 --> nota = "B"
# Si el puntaje es mayor igual a 70 --> nota = "C"
# Si el puntaje es mayor igual a 60 --> nota = "D"
# Si el puntaje es menor a  60      --> nota = "F"

# Recuerde utilizar un solo bloque condicional
# armado de if y múltiples elif
# Puede consultar el ejemplo de clase 2 como referencia

# Imprimir en pantalla la variable nota

nota = int(input('Ingrese nota obtenida en el examen:\n'))

print ('Calificacion Obtenida en Examen')
if nota >= 90:
    print(f'La Calificacion obtenida es "A", con {nota} puntos')
elif nota >= 80 and nota < 90:
    print(f'La Calificacion obtenida es "B", con {nota} puntos')    
elif nota >= 70 and nota < 80:
    print(f'La Calificacion obtenida es "C", con {nota} puntos')
elif nota >= 60 and nota < 70 :
    print(f'La Calificacion obtenida es "D", con {nota} puntos')
else:
    print(f'La Calificacion obtenida es "F", con {nota} puntos')
    
    
    