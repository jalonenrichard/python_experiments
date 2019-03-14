numArray = range(1, 1001)
print(numArray)
print(min(numArray))
print(max(numArray))

evenList = []
oddList = []
for x in numArray:
    if x % 2 == 0:
        evenList.append(x)
    else:
        oddList.append(x)
print(evenList)
print(oddList)
