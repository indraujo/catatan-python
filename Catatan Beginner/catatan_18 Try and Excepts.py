# Try and Except
text = input("Username : ")
try:
    number = int(text)
    print(number)
except:
    print("Invalid Username!")