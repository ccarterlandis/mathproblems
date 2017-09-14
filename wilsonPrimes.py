import math
primeList = []
wilsonList = []
def findWilson(i):
    w = math.factorial(i-1)
    w += 1
    if w%i == 0:
        primeList.append(i)
        w = w/i
        if w%i == 0:
            wilsonList.append(i)

for i in range(2, 1000):
    findWilson(i)

print(primeList)
print(wilsonList)

