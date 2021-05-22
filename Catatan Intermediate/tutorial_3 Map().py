#3 Map function

li = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**x

newList = []
for i in li:
    newList.append(func(i))

print(newList)


#---------

print(list(map(func,li)))

print([func(x) for x in li if x%2==0])

task = [1,2,3,4,5]

def funcs(x):
    print("this is task",x)

list(map(funcs,task))

