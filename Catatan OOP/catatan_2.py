## Create Class
class Dog(object):
    def __init__(self,name,age):
        # attribute
        self.name = name
        self.age = age
        
    def speak(self):
        print("Hi I Am",self.name,"and I am",self.age)

    def chage_age(self,age):
        self.age = age

tim = Dog("tim",6)
tim.speak()
fred = Dog("fred",5)
fred.speak()

