i = input("Enter input file name: ")
f = open(i, "r")
a = c = t = g = 0

str = f.readline()

newStr = str.replace('T','U')

print(newStr)
    