# Optional Parameteres Tutorial #1

def func1(x=5):
    return x **2

def func2(word,add=5,freq=2):
    print(word*(freq+add))

call = func2("indra",0,1)

class car(object):
    def __init__(self,make,model,year,condition="New",kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self,showAll):
        if showAll :
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make,self.model,self.year,self.condition,self.kms))
        else:
            print("this car is a %s %s from %s." %(self.make,self.model,self.year))

whip = car("ford","Fussion",2012)
whip.display(False)