import time
import random
RANGE = 7900000
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
            
test = []
for i in range(RANGE):
    test.append(random.uniform(0,RANGE))
start = time.clock()
mergeSort(test, 0, len(test))
print("test 1", time.clock() - start)

test.clear()
for i in range(RANGE):
    test.append(random.uniform(0,RANGE))
start = time.clock()
mergeSort(test, 0, len(test))
print("test 2", time.clock() - start)
test.clear()
for i in range(RANGE):
    test.append(random.uniform(0,RANGE))
start = time.clock()
mergeSort(test, 0, len(test))
print("test 3", time.clock() - start)
