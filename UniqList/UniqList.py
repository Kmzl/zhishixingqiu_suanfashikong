import time
import random
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
    index = 1
    resultIndex = 0
    while index < len(numList):
        if numList[resultIndex] != numList[index]:
            resultIndex += 1
            numList[resultIndex] = numList[index]
        index += 1
    while len(numList) > resultIndex + 1:
        numList.pop()

def uniqList1(numList):
    if len(numList) == 0:
        return
    result ={}
    left = 0
    right = 1
    while right < len(numList):
        if numList[left] != numList[right]:
            result[numList[left]] = right - left
            left = right
        right += 1
    result[numList[left]] = right - left
    print(result)
    
            
test = []
for i in range(100000):
    test.append(random.randint(0,100000))
                
#start = time.clock()
#mergeSort(test, 0, len(test))
#uniqList(test)
#print(time.clock() - start)

test = [1,1,2,3,4,4,4,5,6,7,7,7,7,7,8,8,9,10,10,10]
uniqList1(test)
