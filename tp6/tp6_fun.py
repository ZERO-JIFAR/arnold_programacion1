
#Ejercicio 1

#Ejercicio 2

#Ejercicio 3

#Ejercicio 4

#Ejercicio 5

#Ejercicio 6
def repeated_name(e_set, h_set):
    repeated_names = set()
    for student in e_set:
        if student in h_set:
            repeated_names.add(student)
    return repeated_names

#Ejercicio 7

#Ejercicio 8
def games_results(goals,col,team):
    tied_counter = 0
    won_counter = 0
    lost_counter = 0
    print()
    for j in range(1,col):
        if team != j:
            print(f'{team} vs. {j} = {goals[team][j]} - {goals[j][team]}')
            if goals[team][j] > goals[j][team]:
                won_counter+=1
                print("Ganó.")
            elif goals[team][j] == goals[j][team]:
                tied_counter += 1
                print("Empató.")
            else:
                lost_counter+=1
                print("Perdió.")
    return (won_counter,tied_counter,lost_counter)

def goals_dif(goals,col,row,team):
    goals_in_favor = 0
    goals_against = 0
    if team in (1,2,3,4,5,6,7,8,9,10):
        for j in range(1,col):
            goals_in_favor += goals[team][j]
        for i in range(1,row):
            goals_against += goals[i][team]
    return (goals_in_favor,goals_against)

def points(results):
    print("\nLos equipos obtienen tres puntos por partido ganado, uno por empatado y cero por perdido. ")
    total = (results[0] * 3) + results[1]
    return total

#Ejercicio 9

#Ejercicio 10
def diagonal(row, col, matrix):
    diag = []
    for r in range(row):
        for c in range(col):
            if r == c:
                diag.append(matrix[r][c])
    return diag

def inverse_diagonal(row,col,matrix):
    inv_diag=[]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r + c == len(matrix)-1:
                inv_diag.append(matrix[r][c])
    return inv_diag

#Ejercicio 11

#Ejercicio 12

#Ejercicio 13
