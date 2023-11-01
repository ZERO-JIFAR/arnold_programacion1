from Motorcycle import Motorcycle

moto1 = Motorcycle('Azul','jif 154', 10, 2,'Yamaha', 2000, '15/10/2000', 180, 175)
moto2 = Motorcycle('Rojo','als 326', 10, 2,'Kawasaki', 1999, '25/12/1999', 200, 340)

print(f'Informacion de la moto {moto1.brand}, Modelo {moto1.model}, Color {moto1.color}, Patente {moto1.tuition}')
print(f'Capasidad en litros {moto1.fuel_liters} l., Cantidad de ruedas: {moto1.num_wheels}, Velosidad maxima {moto1.top_speed} km/h')
print(f'Fecha de fabricacion {moto1.fabrication_date}, Peso {moto1.weight} kg., Estado del motor {moto1.engine}')
print(" ")
print(f'Informacion de la moto {moto2.brand}, Modelo {moto2.model}, Color {moto2.color}, Patente {moto2.tuition}')
print(f'Capasidad en litros {moto2.fuel_liters} l., Cantidad de ruedas: {moto2.num_wheels}, Velosidad maxima {moto2.top_speed} km/h')
print(f'Fecha de fabricacion {moto2.fabrication_date}, Peso {moto2.weight} kg., Estado del motor {moto2.engine}')
print(" ")

#Motos nuevas
print(f'Estado de la moto: {moto1.new_moto}')

#Metodos arrancar y detener
moto1.start()
print(moto1.engine)
moto1.start()
print(moto1.engine)
moto1.stop()
print(moto1.engine)
moto1.stop()
print(moto1.engine)

#Litros y cantidad de ruedas
print(f'Capasidad en Litros: {moto1.fuel_liters}, Cantidad de ruedas: {moto1.num_wheels}')

#Creacion dinamica de un atributo
moto1.price = 2200000
print(f'El precio de la moto {moto1.brand} {moto1.model} es de ${moto1.price}')

#Consultar precio desde metodo
moto1.check_price()
moto2.check_price()