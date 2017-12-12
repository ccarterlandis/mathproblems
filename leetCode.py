# # --------SINGLE NUMBER 1--------
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#
#     myDict = {}
#
#     for x in nums:
#         myDict[x] = 0
#     for x in nums:
#         myDict[x]+=1
#     for x in nums:
#         if myDict[x] == 1:
#             return x
#
#
#
# nums = [1,2,1,2,3,3,4,4,5]
# val = singleNumber(nums)
# print(val)

# # --------SINGLE NUMBER 2--------
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#
#     myDict = {}
#
#     for x in nums:
#         myDict[x] = 0
#     for x in nums:
#         myDict[x]+=1
#     for x in nums:
#         if myDict[x] == 1:
#             return x
#
#
#
# nums = [1,1,1,2,2,2,3,3,3,4,5,5,5]
# val = singleNumber(nums)
# print(val)

# # --------SINGLE NUMBER 3--------
# def singleNumber(nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         myDict = {}
#         LIST = []
#
#         for x in nums:
#             myDict[x] = 0
#         for x in nums:
#             myDict[x]+=1
#         for x in nums:
#             if myDict[x] == 1:
#                 LIST.append(x)
#
#         return LIST

# --------MISSING NUMBER--------
# def missingNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     myDict = {}
#
#     for x in range(0, len(nums)+1):
#         myDict[x] = 0
#     for x in nums:
#         myDict[x] = 1
#     for x in myDict:
#         if myDict[x] == 0:
#             return x
#
# nums = [0, 1, 2, 3, 4, 5, 7]
# val = missingNumber(nums)
# print(val)

# # --------FIND DUPLICATE--------
# def findDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     myDict = {}
#
#     for x in nums:
#         myDict[x] = 0
#     for x in nums:
#         myDict[x]+=1
#         if myDict[x] > 1:
#             return x
#
# nums = [1,2,3,4,4,5,6,8,4]
# val = findDuplicate(nums)
# print(val)

# # --------SET MISMATCH--------
# def findErrorNums(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     myDict = {}
#     LIST = []
#
#     for x in range(1, len(nums)+1):
#         myDict[x] = 0
#     for x in nums:
#         myDict[x]+=1
#     for x in myDict:
#         if myDict[x] > 1:
#             LIST.append(x)
#             break
#     for x in myDict:
#         if myDict[x] == 0:
#             LIST.append(x)
#             break
#     return LIST
#
#
#
#
# nums = [1,1]
# val = findErrorNums(nums)
# print(val)

# # --------CAPITAL USAGE--------
# def detectCapitalUse(word):
#     """
#     :type word: str
#     :rtype: bool
#     """
#     total = 0
#     for x in range(0, len(word)):
#         if word[x].isupper() == True:
#             total+=1
#
#     if total == len(word):
#         return True
#     elif total == 1 and word[0].isupper() == True:
#         return True
#     elif total == 0:
#         return True
#     else:
#         return False
#
# val = detectCapitalUse("united")
# print(val)




# # # --------HAMMING DISTANCE--------
# def hammingDistance(x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         xBin = format(x, 'b').zfill(32)
#         yBin = format(y, 'b').zfill(32)
#
#         count = 0
#         for x in range(0, len(yBin)):
#             if int(xBin[x]) - int(yBin[x]) != 0:
#                 count+=1
#
#         return count
#
# val = hammingDistance(1, 10000)
# print(val)

# # # --------TOTAL HAMMING DISTANCE--------
# def totalhammingDistance(nums):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#
#         def hammingDistance(x, y):
#             xBin = format(x, 'b').zfill(32)
#             yBin = format(y, 'b').zfill(32)
#
#             count = 0
#             for x in range(0, len(yBin)):
#                 if int(xBin[x]) - int(yBin[x]) != 0:
#                     count+=1
#             return count
#
#         totalHam = 0
#
#         for y in range(0, len(nums)-1):
#             for x in range(y+1, len(nums)):
#                 print("{}, {}".format(nums[y], nums[x]))
#                 totalHam+=hammingDistance(nums[y], nums[x])
#
#         return totalHam
#
#
# nums = [4, 14, 2]
# print(totalhammingDistance(nums))

# # --------FIND NTH DIGIT--------
# def findNthDigit(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#
#     # total = 0
#     # result = 0
#     # for item in myList:
#     #     for x in str(item):
#     #        print(x)
#     #        total+=1
#     #        if total == n:
#     #            return x
#
#     x = 1
#     total = 0
#     while(1):
#         for item in str(x):
#             total+=1
#             if total == n:
#                 return int(item)
#         x+=1
#
#
#
# print(findNthDigit(11))
#
#
# --------FIZZ BUZZ--------
def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    list = []

    for x in range(1, n):
        if (x % 5 == 0 and x % 3 == 0):
            list.append("FizzBuzz")
        elif (x % 3 == 0 ):
            list.append("Fizz")
        elif (x % 5 == 0 ):
            list.append("Buzz")
        else:
            list.append(str(x))

    return list

print(fizzBuzz(100))