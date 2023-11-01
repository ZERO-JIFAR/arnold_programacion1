from Classes import *

print("Ejercicio 1.")
per1 = People()
per1.name = str(input("Ingrese su nombre: "))
per1.age = int(input("Ingrese su edad: "))
per1.dni = int(input("Ingrese su DNI: "))
per1.show()
if per1.adult()==True:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("")

print("Ejercicio 2.")
account1=Account(per1,150)
d='I'
account1.show()
while d=='R' or d=='I':
    print("Presione:")
    print("R para retirar dinero")
    print("I para ingresar dinero")
    print("Cualquier letra para finalizar")
    d=str(input("").upper())
    if d=='I':
        money=float(input("Ingrese el monto a ingresar: "))
        account1.get_in(money)
        print("ingreso")
    elif d=='R':
        money=float(input("Ingrese el monto a retirar: "))
        account1.withdraw(money)
        print("retiro")
    else:
        break
account1.show()

print("")

print("Ejercicio 3")
ingreso1 = int(input("Coloque el valor del primer lado: "))
ingreso2 = int(input("Coloque el valor del segundo lado: "))
ingreso3 = int(input("Coloque el valor del tercer lado: "))
triang1 = Triangulo(ingreso1, ingreso2, ingreso3)
#Accedemos a los atributos del objeto
print(f' Valor del 1° lado: {triang1.lado1}, Valor del 2° lado: {triang1.lado2}, Valor del 3° lado: {triang1.lado3}')
triang1.imprimir_lado_mayor()
triang1.determinar_tipo_triangulo()

print("")

print("Ejercicio 4")
user = Contact()
contact_list = []
while True: 
    print('1. Añadir contacto\n2. Lista de contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda')
    option = input('Elija una opcion: ')
    if option in ('1','2','3','4','5'):
        if option == '1':
            contact_list = user.add_contact(contact_list)
        elif option == '2':
            user.show_list(contact_list)
        elif option == '3':
            user.contact_search(contact_list)
        elif option == '4':
            print('hola')
        else:
            print('Agenda cerrada.')
            break
    else:
        print('Elija una opcion correcta.')