
def Rabbits(n, k):
    if n == 1 or n == 2: return 1
    return Rabbits(n-1, k) + k * Rabbits(n-2, k)
    

i = input("Enter input file name: ")
f = open(i, "r")


str = f.readline()
ints = [int(x) for x in str.split()]

totalRabbits = Rabbits(ints[0], ints[1])
print(totalRabbits)
