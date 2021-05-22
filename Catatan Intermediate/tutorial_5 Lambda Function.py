#5 Lambda Function

def func(x):
    return x+5

func2 = lambda x: x+5
print(func2(9))
print(func(2))

#-------------------
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85

print(func(2))

#------------------
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85
func3 = lambda x,y=4:x+y
print(func3(5))
print(func(2))

#------------------
a = [1,2,3,4,5,6,7,8,9,10]
newList = list(filter(lambda x: x%2==False,a))
print(newList)
