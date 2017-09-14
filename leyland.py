leyNums = []

end = input("Pick a number. ")

def Leyland(q,w):
    num = pow(q,w) + pow(w,q)
    return(num)

for x in range(2, int(end)):
    #print("W = {}".format(x))
    for y in range(2, int(end)):
        #print("Q = {}".format(y))
        if x >= y:
            leyNums.append(Leyland(x,y))

leyNums = sorted(leyNums)
print("The first {} Leyland Numbers are: {}".format(len(leyNums), leyNums))

leyPrimes = []
primes = []

for x in range(2, leyNums[-1]):
    primality = 1
    for y in range(2, x+1):
        if (x % y == 0) & (x != y):
            primality = 0
            break
        if (x == y) & (primality == 1):
            primes.append(y)

for item in primes:
    for thing in leyNums:
        if item == thing:
            leyPrimes.append(thing)

leyPrimes = sorted(leyPrimes)
print(leyPrimes)
#print("The first {} Leyland Primes are: {}".format(len(leyPrimes), leyPrimes))