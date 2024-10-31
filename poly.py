
class Vehicle:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Can Drive")

class Car(Vehicle):
    pass

class Plane(Vehicle):      
    def move(self):
        print("can Fly")


car1 = Car("Ford", "Mustang")
plane1 = Plane("Boeng", "707")

for x in (car1, plane1):
    print(x.brand)
    print(x.model)
    x.move()