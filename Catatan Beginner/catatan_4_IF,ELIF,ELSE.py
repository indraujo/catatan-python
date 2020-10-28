## Condition
'''
if condition == True:
    do this
'''

age = input("Berapa umur kamu?")
age = int(age)
print(type(age))
if age == 16:
    print("Your age 16")
elif age > 16:
    print("Your age >15")
elif age < 16:
    print("Your age <15")
else:
    print("Kamu tidak memasukkan dengan benar")