# Class and Objects
x = "string"
y = 23
boo = True
#print(x.count(x))

class number():
    def __init__(self,num):
        self.var = num
    
    def display(self,x):
        print(x)

num = number(23)
#print(num)
num.display(num.var)