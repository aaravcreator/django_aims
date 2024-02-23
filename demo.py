
import random
class Vehicle():
    id = None
    def __init__(self,name=None,model=None):
        self.name = name
        self.model = model
        self.id = random.randint(1,5)

    def info(self):
        print(f"Name is {self.name} model is {self.model}")
    
class Car(Vehicle):
    def info(self):
        print(f"ID {self.id}. I am car my name is  {self.name} model is {self.model}")
    def __str__(self):
        return f"{self.name}"


car = Car("TATA","NEXON EV")
print(car)
car.info()