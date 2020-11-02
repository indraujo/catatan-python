## Class and Object
# parent
class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am",self.name,"and I am",self.age,"years old")

    def talk(self):
        print("Bark!")

# Cat inherit Dog
class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def talk(self):
        print("Meow!")

jim = Dog("Jim",7)
jim.talk()
tim = Cat("Tim",5,"Blue")
tim.speak()



class Vehicle():
    def __init__(self,price,gas,color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def empyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self,price,gas,color,speed):
        super().__init__(price,gas,color)
        self.speed = speed

    def beep(self):
        print("beep beep")

class Truck(Car):
    def __init__(self,price,gas,color,tires):
        super().__init__(price,gas,color,tires)
        self.tires = tires

    def beep(self):
        print("honk honk")
        
truck = Truck(2000,50,"Blue","DUnlop")