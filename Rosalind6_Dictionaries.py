i = input("Enter input file name: ")
f = open(i, "r")

str = f.readline()
d = {}
for word in str.split(' '):
    d.setdefault(word, 0)
    d[word] = d.get(word) + 1

for key, value in d.items():
    print(key, end=" ")
    print(value)
    
    
