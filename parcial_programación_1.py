name = str(input("Ingrese su nombre: ")).capitalize()

#Inicializar los contadores
pair = 0
odd = 0
acc = 0
acc_a = 0
acc_e = 0
acc_i = 0
acc_o = 0
acc_u = 0

#Eleccion de los juegos
while True:
    print("A qué quieres juagar",name,"?")
    print("0 - Para salir")
    print("1 - Juego de numeros")
    print("2 - Juego de palabras")
    choice = int(input("Selecciona un juego: "))

    #Eleccion de salidad del codigo
    if choice==0:
        print("Hasta pronto",name)
        break

    #Eleccion del juego de numeros
    elif choice==1:
        while True:
            print("Muy bien",name)
            num = int(input("Ingrese un numero entero (0 para salir): "))

            #Condicion de salida
            if num == 0:
                print(name,"el mayor numero par es:", pair)
                print(name,"el promedio de numeros primos es de:",odd/acc)
                break

            #Condicion de nueros par
            elif num % 2==0:
                if pair < num:
                    pair = num

            #Condicion de nueros impar
            elif num % 2 != 0:
                odd += num
                acc += 1

    #Eleccion del juego de palabras
    elif choice==2:
        print("Muy bien",name)
        phrase = str(input("Ingresa una frase: ")).upper()

        #Suma de los contadores
        for letter in phrase:
            letter = letter.lower()
            if letter == "a":
                acc_a += 1
            elif letter == "e":
                acc_e += 1
            elif letter == "i":
                acc_i += 1
            elif letter == "o":
                acc_o += 1
            elif letter == "u":
                acc_u += 1

        #Mostrar las sumas
        print(name,"estas son las cantidades de vocales que habian en tu frase:")
        print("a: ",acc_a)
        print("e: ",acc_e)
        print("i: ",acc_i)
        print("o: ",acc_o)
        print("u: ",acc_u)

    else:
        print(name,"has ingresado un valor invalido")

