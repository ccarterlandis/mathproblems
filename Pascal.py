# 1
# 1,1
# 1,2,1
# 1,3,3,1
# 1,4,6,4,1

global rowAbove
rowAbove = [1,3,3,1]


row1 = [1]
row2 = [1,1]


def rowN(n,w):
    rowCurrent = []
    for item in rowAbove:
        rowCurrent.append(item)
    rowCurrent[n+w:+w] = ((rowAbove[n] + rowAbove[n+1]),0)

    rowCurrent.remove(0)

    print(rowCurrent)

    del rowAbove[:]

    print(rowAbove)

    for item in rowCurrent:
        rowAbove.append(item)


for n in range(0,1):
    w = n +1
    rowN(n,w)