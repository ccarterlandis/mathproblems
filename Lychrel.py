# 196-algorithm

query = input('Pick a 2 or 3 digit number. ')
print(query
      )
def reverse(num):
  return (int(str(num)[::-1]))

def reverseTest(num):
    return (int(str(num)[::-1])) == num

test = reverse(query) + query
count = 1

print(test)
while reverseTest(test) == False:
    print(reverse(test) + test)
    test = reverse(test) + test
    count += 1

print(count)