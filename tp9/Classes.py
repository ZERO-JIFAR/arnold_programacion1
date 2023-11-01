
#1
class People:
    def __init__(self, name='', age=0, dni=0):
        self.__name=name
        self.__age=age
        self.__dni=dni
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,dni):
        self.__dni = dni
    def show(self):
        print(f'Nombre: {self.name}, Edad: {self.age}, DNI: {self.dni}')
    def adult(self):
        if self.age>17:
            return True
        else:
            return False

#2
class Account:
    def __init__(self, owner, amount=0):
        self.__owner=owner
        self.__amount=amount
    
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,amount):
        self.__amount = amount
    
    def show(self):
        print("Propietario:")
        print(f'Nombre: {self.__owner.name}, Saldo: {self.amount}')
    
    def get_in(self, money):
        self.amount+=money
        
    def withdraw(self, money):
        self.amount-=money

#3
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        #Atributos de instancia
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def imprimir_lado_mayor(self):
        max_lado = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {max_lado}")
    def determinar_tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")

#4
class Contact:
    def __init__ (self,name='',tel=0,email=''):
        self.__name = name
        self.__tel = tel
        self.__email = email
    # Getter
    @property
    def name(self):
        return self.__name
    # Setter
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self, tel):
        self.__tel = tel
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    def add_contact(self,contact_list):
        self.name = input('Nombre: ').lower()
        self.tel = int(input('Telefono: '))
        self.email = input('Mail:  ')
        contact_list.append(self)
        return contact_list
    def show_list(self,contact_list):
        for i in contact_list:
            print(f'{self.name}\n{self.tel}\n{self.email}')
    def contact_search(self,contact_list):
        person = input('Ingrese el nombre del contacto que quiere buscar: ').lower()
        for i in contact_list:
            if i.name == person:
                print(f'{self.name}\m{self.tel}\n{self.email}')