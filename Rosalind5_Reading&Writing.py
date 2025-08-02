i = input("Enter input file name: ")
o = input("Enter output file name: ")
f = open(i, "r")
g = open(o, "w")
j = 1

while(j < 1001):
    next_Line = f.readline()
    if next_Line:
        if j%2 == 0:
            g.write(next_Line)
        j += 1
    else:
        break

f.close()
g.close()
