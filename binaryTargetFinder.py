list = []
for x in range(0, 10000000):
    list.append(x)

target = int(input("Pick a number from to 10000000. "))
mid = list[int(len(list)/2)]
count = 0
found = 1

while (mid != target):
    mid = list[int(len(list)/2)]
    print("Mid is {}.".format(mid))
    if mid > target:
        list = [x for x in list if x <= mid]
        print("The upper half of the list has been removed, and is now {}.".format(list))
    elif mid < target:
        list = [x for x in list if x >= mid]
        print("The lower of half of the list has been removed, and is now {}.".format(list))
    if len(list) == 1:
        found = 0
        break
    count += 1

if found == 0:
    print("The target value was not found.")
else:
    print("The target value was {}.".format(mid))

print("{} comparisons performed.".format(count))
