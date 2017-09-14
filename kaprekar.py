query = input('Pick a 4 digit number where every digit is not the same digit (i.e. 1111 or 2222.) ')

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

result1 = int(asc(query))
result2 = int(dec(query))
final = (result2 - result1)
count = 0
while final != 6174:
    result1 = int(asc(final))
    result2 = int(dec(final))
    final = (result2 - result1)
    if final == 0:
        break
    count += 1
    print(final)
print(count)