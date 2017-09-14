import time


end = input('Pick a number. ')

start_time = time.time()

allNums = []
for x in range(0, end+1):
    allNums.append(x)

mid = 0
sum = 0

for x in allNums:
    for y in str(x):
        sum = sum + int(y)

print("The sum of all the digits of the numbers between 1 and {} is {}.".format(end, sum))
print("--- %.6s seconds ---" % (time.time() - start_time))