import math
i = input("Enter file name: ")
with open(i, "r") as file:
    x = file.readline().split()
    a = int(x[0])
    b = int(x[1])
    sum = 0
    for i in range(a, b+1):
        if(i % 2 == 1):
            sum += i
        
    print(sum)
    
    
