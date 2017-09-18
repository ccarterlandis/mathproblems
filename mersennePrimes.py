import time

list = []

end = input("How many Mersenne primes would you like to find? ")

start_time = time.time()

def mersenneFind(n):
    ms = (2**n)-1
    count = 0
    for i in range(2, ms-1):
        if ms%i==0:
            count += 1
    if count==0:
        list.append(ms)

w = 1
while len(list) != end:
    mersenneFind(w)
    print(w)
    w+=1

print("The first {} Mersennse primes are {}.".format(len(list), list))
print("--- %.6s seconds ---" % (time.time() - start_time))