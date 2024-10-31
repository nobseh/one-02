
class Vehicle:
    def __init__(self, make, model):
        self.make = make 
        self.model = model 

    def move(self):
        return f'Can Drive!'
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        return f'Can Sail!'
    
class Plane(Vehicle):
    def move(self):
        return f'Can Fly!'

car1 = Car('Ford', 'Mustang')
boat1 = Boat('Ibiza', 'T15')
plane1 = Plane('Boean', 707)

for x in (car1, boat1, plane1):
    print(x.make, x.model)
    print(x.move())
    print('\n')
    

