end = input('Pick a number. ')

allNums = []
for i in range(2, end):
    allNums.append(i)

factors = []
result = 0
w = 1

for x in range(2,10):
    factors = []
    while x*w <= end:
        factors.append(x*w)
        w+=1
    for y in allNums:
        for item in factors[1::]:
            if y == item:
                allNums.remove(y)
    w = 1

print("All the primes between 2 and {} are {}.".format(end, allNums))