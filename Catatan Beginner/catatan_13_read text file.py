# Read Text
# r = read
# w = write
file = open("Hello.txt","r")
f = file.readlines()
newList = []
for line in f:
    if line[-1] == "\n":
        newList.append(line[:-1])
    else:
        newList.append(line)

    newList.append(line.strip())
print(newList)