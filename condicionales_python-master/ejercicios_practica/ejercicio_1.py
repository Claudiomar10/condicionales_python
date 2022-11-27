# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Objetivo:
# Ingrese dos números enteros cualesquiera
# y realice las siguientes comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable

# Compare los dos números y entre sí 
# utilizando if y else.
# - Si numero_1 es mayor a numero_2, almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
res_1 = 0
if numero_1 > numero_2:
    res_1 = numero_1
    print (f"El numero mayor es = {res_1}")
elif numero_1 < numero_2:
    res_1 = numero_2
    print (f"El numero mayor es = {res_1}")
else:
    print (f"El numero_1 ={numero_1} y el numero_2 ={numero_2} son iguales")

# Imprimir en pantalla la variable res_1


# Verifique si el numero_1 positivo, negativo o cero
# Utilice if, elif y else
# - Si numero_1 es positivo, almacenar 1 en res_2
# - Si numero_1 es negativo, almacenar 2 en res_2
# - Si numero_1 es cero, almacenar 3 en res_2
res_2 = 0
if numero_1 > 0:
    res_2 = numero_1
    print(f"El {res_2} es positivo")
elif numero_1 <0:
    res_2 = numero_1
    print(f'El {res_2} es negativo')
else:
    print(f'El primer numero ingresado es igual a cero')
     
# Imprimir en pantalla la variable res_2


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3
if numero_1 > 0 and numero_1< 100:
    res_3 = numero_1
    print (f'El primer numero ingresado,{res_3},cumple la condicion')
else:
    res_3 = numero_2
    print(f'El primer numero ingresado no cumple la condicion, se almacena el segundo numero,{res_3}')
# Imprimir en pantalla la variable res_3


# Verifique si:
# el numero_1 es menor a 10 o el numero_2 es mayor a -2
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_4
# - De lo contrario, almacenar 2 en res_4
if numero_1 < 10 or numero_2 > -2:
    res_4 = numero_1
    print (f'Se cumple la condicion, se almacena el primer numero ingresado,{res_4}')
else:
    res_4 = numero_2
    print (f'No se cumple la condición, se almacena el segundo numero ingresado,{res_4}')
    


# Imprimir en pantalla la variable res_4
