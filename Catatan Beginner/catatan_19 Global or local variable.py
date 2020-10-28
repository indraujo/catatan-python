# Global VS Local (specific) variable
# Global variable out of the functiona
# specifiec variable is ini the function
v = 9
loop = True
def func(x):
    global loop
    loop = 7
    if x == 5:
        return x

print(func(5))

def otherFunc():
    newVar = 5
    print(newVar)

func(2)
print(loop)