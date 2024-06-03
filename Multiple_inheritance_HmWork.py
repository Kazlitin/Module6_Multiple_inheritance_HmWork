class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return "Лошадиные силы не определены"

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Nissan"
        self.price = 1500000  # У Nissan цена выше

    def horse_powers(self):
        return "Nissan обычно имеет около 150-200 лошадиных сил"

# Создаю экземпляр класса Nissan
my_nissan = Nissan()

print(my_nissan.vehicle_type, my_nissan.price)