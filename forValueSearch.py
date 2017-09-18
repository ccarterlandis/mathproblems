import time

name = input("Please enter your name: ")
print("")
lower = name.lower()
sum = 0
for ch in lower:
    sum+=(ord(ch)-96)

sum *= 400

list = []
for x in range(0, 100000):
    list.append(x)

found = 0
count = 0

start_time = time.time()

while count != 10000000:
    if count == sum:
        found = 1
        break
    count+=1

if found == 1:
    print("\nYour name, {}, in contained in the set 0 to 100.".format(name))
    print("--- %.10s seconds ---" % (time.time() - start_time))
else:
    print("\nYour name is not contained in the set 0 to 100.")
    print("--- %.10s seconds ---" % (time.time() - start_time))