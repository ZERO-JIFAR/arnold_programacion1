import tp9_fun as tp9_fun

# Ejemplo de no mutante
#matrix = ['atgcga','cagtgc','ttattt','agacgg','gcgtca','tcactg']
# Ejemplo de mutante
#matrix = ['atgcga','cagtgc','ttatgt','agaagg','ccccta','tcactg']

# Pedir al usuario el ingreso de datos
print("Ingrese las filas de la matriz de 6x6 (solo ATCG):")

# Comentar las siguientes 4 lineas para trabajar con los ejemplos
matrix = []
for _ in range(6):
    row = input()
    matrix.append(row)

# Dar formato y transformar la matriz (no importa si son mayusculas o minusculas)
formatted_matrix = tp9_fun.format_input(matrix)

tp9_fun.is_mutant(formatted_matrix)
