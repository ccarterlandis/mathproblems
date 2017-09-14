sequence = [1]

n = 0

while n < 40:
    sequence.append(sequence[n] + sequence[n-1])
    n += 1

print('The Fibonacci sequence, up to the 30th term, is \n' + str(sequence) + '.')

pisano = input("Please pick a number. ")

psequence = []

for item in sequence:
    psequence.append(item % pisano)
print(psequence)
# for item in sequence:
#     if item%pisano != 0:
#         psequence.append(item%pisano)
#     else:
#         print('The Pisano period of ' + str(pisano) + ' for the Fibonacci sequence is ' + str(psequence) + '.')
#         break




