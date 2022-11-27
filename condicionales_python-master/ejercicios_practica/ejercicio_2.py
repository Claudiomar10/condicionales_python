# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Objetivo:
# Ingrese dos palabras cualesquiera
# y realice las sigueintes comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

'''tome la determinacion de pasar los dos textos a mayusculas a efectos
de poder comparar las palabras, para  que tengan la misma jerarquía '''
texto_1 = texto_1.upper()
texto_2 = texto_2.upper()
print (texto_1)
print (texto_2)

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable o la cree con ese valor

# Compare las dos palabras y entre sí 
# utilizando if y else.
# - Si texto_1 es mayor (alfabéticamente) a texto_2, 
#   almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
if texto_1 > texto_2:
    res_1 = texto_1
    print(f'{texto_1} esta despues que {texto_2} en el orden alfabetico')
elif texto_1 < texto_2:
    print(f'{texto_2} esta despues que {texto_1} en el orden alfabetico')
else:
    print('las dos palabras ingresadas son iguales')


# Imprimir en pantalla la variable res_1

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Utilice if, elif y else
# - Si texto_1 tiene más letras, almacenar 1 en res_2
# - Si texto_2 tiene más letras, almacenar 2 en res_2
# - Si tienen la misma cantidad de letras, almacenar 3 en res_2
if len(texto_1) > len(texto_2):
    print(f'{texto_1} tiene mas letras que {texto_2}')
elif len(texto_1) < len(texto_2):
    print(f'{texto_2} tiene mas letras que {texto_1}')
else:
    print(f'Las dos palabras ingresadas tienen la misma cantidad de letras')
    
    

# Imprimir en pantalla la variable res_2

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# - Si la primera letra de texto_1 es mayor,
#   almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3
if texto_1[0] > texto_2[0]:
    print(f'La primera letra de {texto_1} es mayor que la primera letra de {texto_2}')
elif texto_1[0] < texto_2[0]:
    print(f'La primera letra de {texto_2} es mayor que la primera letra de {texto_1}')
else:
    print(f'Las dos primeras letras de las palabras ingresadas son iguales')



# Imprimir en pantalla la variable res_3

