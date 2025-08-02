i = input("Enter input file name: ")
f = open(i, "r")

def gcContent(strand):
    a = 0
    for char in strand:
        if char == 'G' or char == 'C':
            a += 1
    return a / len(strand)


ids = []
strings = []
maxGC = 0
maxID = -1

current_strand = ""

for line in f:
    line = line.strip()
    if line.startswith('>'):
        if current_strand != "":
            strings.append(current_strand)
            current_strand = ""
        ids.append(line[1:])
    else:
        current_strand += line 

if current_strand != "":
    strings.append(current_strand)


for element in strings:
    currentGC = gcContent(element)
    if currentGC > maxGC: maxGC = currentGC; maxID = strings.index(element)

print(ids[maxID])
print(maxGC * 100)
    
