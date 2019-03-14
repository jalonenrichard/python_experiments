def sortList(inputList):
    inputList.sort()
    return inputList
def secondParamSort(param):
    return param[1]

x =[(3,6),(4,7),(5,9),(8,4),(3,1)]
print(sortList(x))
x.sort(key=secondParamSort)
print(x)
