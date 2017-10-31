def merge(numList, firstIndex, midIndex, endIndex):
    left = numList[firstIndex:midIndex]+[float("inf")]
    right = numList[midIndex:endIndex]+[float("inf")]
    leftIndex = 0
    rightIndex = 0
    for i in range(firstIndex, endIndex):
        if left[leftIndex] < right[rightIndex]:
            numList[i] = left[leftIndex]
            leftIndex += 1
        else:
            numList[i] = right[rightIndex]
            rightIndex += 1

def mergeSort(numList, firstIndex, endIndex):
    if endIndex - firstIndex > 1:
        midIndex = int((firstIndex + endIndex) / 2)
        mergeSort(numList, firstIndex, midIndex)
        mergeSort(numList, midIndex, endIndex)
        merge(numList,firstIndex, midIndex, endIndex)

def uniqList(numList):
    if len(numList) == 0:
        return
    index = 0
    while index + 1 < len(numList):
        if numList[index] == numList[index + 1]:
            del numList[index + 1]
        else:
            index += 1
            
test = [6,1,3,4,6,5,3,5,1,2]
mergeSort(test, 0, len(test))
uniqList(test)
print(test)