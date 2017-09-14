list = []
for x in range(0, 10000000):
    list.append(x)

target = int(input("Pick a number from to 10000000. "))
mid = list[int(len(list)/2)]

while (mid != target):
    mid = list[int(len(list)/2)]
    print("Mid is {}.".format(mid))
    if mid > target:
        list = [x for x in list if x <= mid]
        print("The upper half of list has been removed, and is now {}.".format(list))
    elif mid < target:
        list = [x for x in list if x >= mid]
        print("The lower of list has been removed, and is now {}.".format(list))

print("The target value was {}.".format(mid))
