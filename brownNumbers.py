import math

allBrown = []

def brown(m,n):
    brownMid = []
    nResult = math.factorial(n) + 1
    mResult = pow(m,2)
    if mResult == nResult:
        brownMid.append(m)
        brownMid.append(n)
    if brownMid:
        allBrown.append(brownMid)

for x in range(100):
    for y in range(100):
        brown(x,y)

print(allBrown)

print("The first {} pairs of Brown numbers are {}.".format(len(allBrown), allBrown))
