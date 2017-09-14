userInt = input("Pick a number. ")
counter, primality, lower = 0, 0, 0
primeList = []
for x in range(2, int(userInt)):
    primality = 1
    for y in range(2, x+1):
        if (x % y == 0) & (x != y):
            primality = 0
            break
        if (x == y) & (primality == 1):
            print("{} is prime.".format(y))
            primeList.append(y)

print("There are {} primes below {}.".format(len(primeList), userInt))