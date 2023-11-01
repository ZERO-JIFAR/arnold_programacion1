class Motorcycle:
    new_moto='nueva'
    engine=False

    def __init__(self, color='', tuition='', fuel_liters=0, num_wheels=0, brand='', model=0, fabrication_date='', top_speed=0, weight=0):
        self.color=color
        self.tuition=tuition
        self.fuel_liters=fuel_liters
        self.num_wheels=num_wheels
        self.brand=brand
        self.model=model
        self.fabrication_date=fabrication_date
        self.top_speed=top_speed
        self.weight=weight

    def start(self):
        if self.engine==False:
            self.engine=True
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")
    
    def stop(self):
        if self.engine==True:
            self.engine=False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")

    def check_price(self):
        print(f'El precio de la moto {self.brand} {self.model} es de ${self.price}.')