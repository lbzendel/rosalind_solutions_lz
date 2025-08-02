i = input("Enter input file name: ")
f = open(i, "r")
a = c = t = g = 0

str = f.readline()

for char in str:
    if char == 'A':
        a += 1
    elif char == 'C':
        c += 1
    elif char == 'T':
        t += 1
    elif char == 'G':
        g += 1

print(a, c, g, t)
    
