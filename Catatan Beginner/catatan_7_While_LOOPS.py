## While Loops
'''
while conditions:
    do this
'''
loop = True
while loop:
    password = input("insert password:")
    if password!="admins123":
        print("Wrong password!!!")
    elif password=="admins123":
        print("Welcome")
        loop = False
        break

