class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sails")

class Plane(Vehicle):
    def move(self):
        print("flies")

car=Car("Ford","raptor")
boat=Boat("Ibiza","rav")
plane=Plane("boeing","878")

for x in (car,boat,plane):
    print("Brand: ",x.brand)
    print("Model: ",x.model)