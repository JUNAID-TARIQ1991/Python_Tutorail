class Automobile:
    def __init__(self, make, model, milage, price):
        self.__make = make
        self.__model = model
        self.__milage = milage
        self.__price = price

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def milage(self):
        return self.__milage

    @property
    def price(self):
        return self.__price


class Car(Automobile):
    def __init__(self, Type, doors, make, model, milage, price):
        self.__door = doors
        self.__type = Type
        super().__init__(make, model, milage, price)

    @property
    def doors(self):
        return self.__door

    @property
    def type(self):
        return self.__type


car1 = Car("sedan", 4, "Toyota", 2021, '12Km', 2500)
print(car1.price)
print(car1.milage)
print(dir(Automobile))
