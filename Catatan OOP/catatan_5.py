## Static Method and class methods
class Dog:
    dogs = []
    
    def __init__(self,name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """bark n times"""
        for _ in range (n):
            print("Bark!")

tim = Dog("Tim")
jim = Dog("Jim")
print(Dog.dogs)