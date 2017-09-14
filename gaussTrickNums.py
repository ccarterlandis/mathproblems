end = input('Pick a number. ')
allNums = []
for x in range(0, end+1):
    allNums.append(x)

count = 1
sum = 0
for y in range(0, (len(allNums)-1)/2):
    sum = sum + (allNums[count] + allNums[-count])
    count += 1

print("The sum of all numbers between 1 and {} is {}.".format(end, sum))