import matplotlib.pyplot as plt


def asc(query):
    bTs = str(query)
    new = []
    for item in (sorted(bTs, key=int)):
        new.append(item)
    b = ''.join(new)
    return(b)

def dec(query):
    sTb = str(query)
    new2 = []
    for item in (sorted(sTb, key=int, reverse=True)):
        new2.append(item)
    s = ''.join(new2)
    return(s)

allcount =[]
sixcount = []
fivecount = []
for query in range(1000, 1035, 1):
    count = 0
    result1 = int(asc(query))
    result2 = int(dec(query))
    final = (result2 - result1)
    while final != 6174:
        result1 = int(asc(final))
        result2 = int(dec(final))
        final = (result2 - result1)
        if final == 0:
            break
        count += 1
    allcount.append(count)
    sixcount.append(6-count)
    fivecount.append(5-count)
    count = 0


plt.subplot(111, axisbg='black')
width = 3
plt.plot(allcount, linewidth=width)
plt.plot(sixcount, linewidth=width)
plt.plot(fivecount, linewidth=width)
plt.plot(allcount[::-1], linewidth=width)
plt.plot(sixcount[::-1], linewidth=width)
plt.plot(fivecount[::-1], linewidth=width)
plt.show()