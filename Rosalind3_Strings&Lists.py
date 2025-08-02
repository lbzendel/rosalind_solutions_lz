import math
integers = []
with open("Rosalind Strings and Lists.txt", "r") as file:
    s = file.readline()
    ints = file.readline()
    x = ints.split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    slice1 = s[a : b+1]
    slice2 = s[c : d+1]
    combined = slice1 + " " + slice2
    print(combined)
    
