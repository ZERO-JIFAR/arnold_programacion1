print ("Bienvenido a tu tienda online")
total=0
prod_list=["1 - Paquete de Fideos","2 - Caja de Tomate","3 - Kg de Carne molida","4 - g de Oregano","0 - salir"]
while True:
    print("Que deseas comprar")
    for i in prod_list:
        print(i)
    prod=int(input("Seleccione un objeto: "))
    if prod == 0:
        break
    elif prod == 1:
        cant=int(input("Cauntos Paquete de Fideos vas a llevar? "))
        total+=cant*100
        print("")
    elif prod == 2:
        cant=int(input("Cuantos Cajas de Tomate vas a llevar? "))
        total+=cant*200
        print("")
    elif prod == 3:
        cant=float(input("Cauntos Kg de Carne molida vas a llevar? "))
        total+=cant*150
        print("")
    elif prod == 4:
        cant=float(input("Cauntos g de Oregano vas a llevar? "))
        total+=cant*10
        print("")
    else:
        print("Ingrese un numero valido")
        print("")
if total>1000:
    print("Felicidades tienes envio gratis")
    print("El total a pagar es de $",total)
else:
    print("El total a pagar es de $",total) 