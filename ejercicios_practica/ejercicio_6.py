# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia:'))
fin = int(input('Ingrese el último número de la secuencia:'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0

# for ... in range(....)

cant_may_cero = 0
cant_negativos = 0
cant_positivos = 0

for numero in range(inicio,fin+1):
    if numero >= 0:                     # Número mayor que 0
        cant_may_cero += 1              
        if(numero % 2) == 0:            # Número positivo
            cant_negativos += 1         
        else:                           # Número negativo
            cant_positivos += 1         
print("Cantidad de números mayores que cero:",cant_may_cero)
print("Cantidad de números negativos:",cant_negativos)
print("Cantidad de números positivos:",cant_positivos)

# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
