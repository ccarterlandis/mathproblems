import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

end = input("Pick a number. ")

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

count1 = 0
count3 = 0
count7 = 0
count9 = 0

print(allNums)

for item in allNums:
    print(str(item)[-1])
    if str(item)[-1] == '1':
        count1+=1

for item in allNums:
    print(str(item)[-1])
    if str(item)[-1] == '3':
        count3+=1

for item in allNums:
    print(str(item)[-1])
    if str(item)[-1] == '7':
        count7+=1

for item in allNums:
    print(str(item)[-1])
    if str(item)[-1] == '9':
        count9+=1

print("Primes whose last number is 1 appear {} times, those whose last number is 3 appear {} times,those whose last "
      "number is 7 appear {} times, and those whose last number is 9 appear {} times.".format(count1, count3, count7, count9))

plt.subplot(111, axisbg='black')

objects = ('1', '3', '7', '9')
y_pos = np.arange(len(objects))
digits = [count1, count3, count7, count9]

plt.bar(y_pos, digits, align='center', alpha=0.5, color='yellow')
plt.xticks(y_pos, objects)
plt.ylabel('Number of Occurences')
plt.title('Last digits of prime numbers less than {}'.format(end))

plt.show()
