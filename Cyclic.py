query = input('Pick a number less than the magnitude of 10^8. Note- any multiple of 7 will give an unusual answer. Use a number that is not a multiple '
              'of 7 for the best results. ')

print('\nYou have picked the number ' + str(query) + '. To demonstrate the cyclic nature of the number 142857, let\'s '
                                                   'begin by multiplying ' + str(query) + ' and 142857.')

var1 = 142857 * query

if len(str(var1)) == 6:
    print('\nThis gives us a result of ' + str(var1) + ', which is a permutation of 142857.')
    #FIGURE OUT HOW TO STOP CODE HERE

def last6(num):
    return int(str(num)[len(str(num)) - 6::])

def firstNums(num):
    return int(str(num)[:len(str(num)) - 6])


result = (firstNums(var1) + last6(var1))

print('\nThis gives us the result ' + str(var1) + '.')

print('\nNext, we add the last 6 digits, which are ' + str(last6(var1)) + ', to the remaining digits in front, which in '
                                                                        'this case is ' + str(firstNums(var1)) + '.')

if 0 != query % 7:
    print('\nThis gives us a result of ' + str(result) + ', which is a permutation of 142857.')
else:
    print('\nThis gives us a result of ' + str(result) + ', which is not a permutation of 142857! Any multiple of 7 will '
                                                       'cause a result of a repeating sequence of 9s. ')
