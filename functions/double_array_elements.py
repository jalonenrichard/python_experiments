def doubleEachElement(array):
    outputArray = []  
    for element in array:
        outputArray.append(element)
        outputArray.append(element * 2)
    outputArray.sort()
    return outputArray

array = [6,4,2]
print(doubleEachElement(array))
