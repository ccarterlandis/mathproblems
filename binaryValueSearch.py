name = input("Please enter your name: ")
lower = name.lower()
sum = 0
for ch in lower:
    sum+=(ord(ch)-96)

list = []
for x in range(0, 100):
    list.append(x)
mid = list[int(len(list)/2)]
found = 1

while (mid != sum):
    mid = list[int(len(list)/2)]
    print("Mid is {}.".format(mid))
    if mid > sum:
        list = [x for x in list if x <= mid]
        print("The upper half of list has been removed, and is now {}.\n".format(list))
    elif mid < sum:
        list = [x for x in list if x >= mid]
        print("The lower of list has been removed, and is now {}.\n".format(list))
    if len(list) == 1:
        found = 0
        break

if found == 1:
    print("\nYour name, {}, in contained in the set 0 to 100.".format(name))
else:
    print("\nYour name is not contained in the set 0 to 100.")