# Perfect numbers are numbers with the property such that the sum of all their factors equals themselves.

perfectNumbers = []
factors = []
for n in range(1, 10000, 1):
    count = 1
    for w in range(0, n):
        if n%count == 0:
            factors.append(count)
        if count < n:
            count+= 1
    sum = 0
    for item in factors[:-1]:
        sum += item
    factors=[]
    if sum == n:
        perfectNumbers.append(n)

print(perfectNumbers)













