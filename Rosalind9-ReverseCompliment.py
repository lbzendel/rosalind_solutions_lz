def complement(x):
    complementStr = ""
    for char in x:
        if char == 'A': complementStr += 'T'
        elif char == 'T': complementStr += 'A'
        elif char == 'G': complementStr += 'C'
        elif char == 'C': complementStr += 'G'
    return complementStr

i = input("Enter input file name: ")
f = open(i, "r")


str = f.readline().strip().upper()
reversed = str[::-1]
revComp = complement(reversed)
print(revComp)


