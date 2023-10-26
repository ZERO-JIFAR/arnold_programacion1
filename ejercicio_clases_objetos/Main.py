from Motorcycle import Motorcycle

my_motorcycle = Motorcycle('Azul','als 154', 10, 2,'Yamaha', 2000, 15/10/2000, 180, 85)

#Accedemos a los atributos del objeto
print(f'Color: {my_motorcycle.color}, Modelo: {my_motorcycle.model}')

#Creación dinámica de un atributo
my_motorcycle.surname = 'Rigoni'
print(f'Atributo creado dinámicamente: {my_motorcycle.surname}')

my_motorcycle.start()
print(my_motorcycle.engine)
my_motorcycle.stop()
print(my_motorcycle.engine)