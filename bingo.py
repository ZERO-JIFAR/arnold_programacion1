import random

def generate_card():
    card = []
    while len(card) < 25:
        number = input(f"Ingrese el {len(card) + 1}° numero (entre 1 y 75): ")
        try:
            number = int(number)
            if number >= 1 and number <= 75 and number not in card:
                card.append(number)
            else:
                print("Ingrese un numero valido y unico (entre 1 y 75)")
        except ValueError:
            print("Ingrese un numero valido")

    return card

def print_card(card):
    for i in range(5):
        for j in range(5):
            print(f"{card[i * 5 + j]:2}", end=" ")
        print()

def play_bingo(card):
    winning_lines = [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14),
                    (15, 16, 17, 18, 19), (20, 21, 22, 23, 24), 
                    (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 17, 22), 
                    (3, 8, 13, 18, 23), (4, 9, 14, 19, 24), 
                    (0, 6, 12, 18, 24), (4, 8, 12, 16, 20)]

    drawn_balls = []
    while True:
        input(f"Presione ENTER para sacar una bola")
        while True:
            ball = random.randint(1, 75)
            if ball not in drawn_balls:
                break
        print(f"Ha salido la bola: {ball}")
        drawn_balls.append(ball)

        if ball in card:
            card[card.index(ball)] = 0

        print_card(card)

        for line in winning_lines:
            if all(card[i] == 0 for i in line):
                print("¡Linea!")
                return

def main():
    print("Bienvenido al Bingo")
    while True:
        card = generate_card()
        print("Tu carton de Bingo:")
        print_card(card)
        play_bingo(card)
        response = input("¿Quieres jugar de nuevo? (s/n): ")
        if response.lower() != 's':
            break

if __name__ == "__main__":
    main()
