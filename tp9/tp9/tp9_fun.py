
# Valida las letras ingresadas
def is_valid_dna(matrix):
    valid_letters = {'A', 'T', 'C', 'G'}
    for row in matrix:
        for letter in row:
            if letter not in valid_letters:
                return False
    return True

# Convierte las letras a mayúsculas y agrega un espacio entre ellas
def format_input(matrix):
    formatted_matrix = [[letter.upper() for letter in row] for row in matrix]
    return formatted_matrix

# Revisa las secuencias horizontales
def check_horizontal(matrix):
    count = 0
    for row in matrix:
        for i in range(len(row) - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                count += 1
    return count

# Revisa las secuencias verticales
def check_vertical(matrix):
    count = 0
    for col in range(len(matrix[0])):
        for i in range(len(matrix) - 3):
            if matrix[i][col] == matrix[i + 1][col] == matrix[i + 2][col] == matrix[i + 3][col]:
                count += 1
    return count

# Revisa las secuencias diagonales
def check_diagonal(matrix):
    count = 0
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 3):
            if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][j + 3]:
                count += 1
    for i in range(len(matrix) - 3):
        for j in range(3, len(matrix[0])):
            if matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][j - 3]:
                count += 1
    return count

# Funcion principal
def is_mutant(dna):
    check_horizontal(dna)
    check_vertical(dna)
    check_diagonal(dna)

    if not is_valid_dna(dna):
        print("La matriz contiene letras invalidas. Solo debe contener 'A', 'T', 'C' o 'G'")
        return 0

    horizontal_count = check_horizontal(dna)
    vertical_count = check_vertical(dna)
    diagonal_count = check_diagonal(dna)

    total_count = horizontal_count + vertical_count + diagonal_count

    if total_count > 1:
# Muetra la matriz con un formato mas limpio
#        for row in dna:
#            print(' '.join(row))
# Muestra la cantidad de secuencias encontradas
#        print(f"Se encontraron {total_count} secuencias de cuatro letras iguales")
        return True
    else:
# Muetra la matriz con un formato mas limpio
#        for row in dna:
#            print(' '.join(row))
        return False
