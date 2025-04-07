class Smartphone:
    def __init__(self, brand, model, number):
        self.phone_brand = brand
        self.phone_model = model
        self.number = number

    def say_brand(self):
        print("Марка телефона", self.brand)

    def say_model(self):
        print("Модель телефона", self.model) 

    def say_number(self):
        print("Номер телефона", self.number)