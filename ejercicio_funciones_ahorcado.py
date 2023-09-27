import random

words = ["rojo", "marron", "amarillo", "azul", "negro", "blanco", "verde", "morado", "violeta", "naranja"]

# Funcion: seleccionar una palabra random
def select_word():
    return random.choice(words)

# Funcion: inicio tablero
def ini_board(word):
    return ['_' for _ in word]

# Funcion: tablero actual
def show_board(board):
    return ' '.join(board)

# Funcion: juego en si
def game():
    secret_word = select_word()
    board = ini_board(secret_word)
    max_attem = 6
    remaining_attem = max_attem
    guessed_letters = []

    print("¡Bienvenido al juego del ahorcado!")
    print("La palabra tiene {} letras.".format(len(secret_word)))

    while True:
        print("\nPalabra actual: {}".format(show_board(board)))
        word = input("Ingresa una letra: ").lower()

        if word in guessed_letters:
            print("Ya adivinaste esa letra.")
            continue

        if word in secret_word:
            print("Adivinaste una letra correctamente.")
            guessed_letters.append(word)
            for i, char in enumerate(secret_word):
                if char == word:
                    board[i] = word
        else:
            print("Letra incorrecta, te quedan {} intentos.".format(remaining_attem))
            remaining_attem -= 1

        if '_' not in board:
            print("\n¡Felicidades! Adivinaste la palabra: {}".format(secret_word))
            break

        if remaining_attem == 0:
            print("\n¡Perdiste! La palabra era: {}".format(secret_word))
            break

if __name__ == "__main__":
    game()
