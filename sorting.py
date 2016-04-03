#Sorting algoritms written in Pyhton
#Mainly for IB002


#INSERTION SORT
def insert_sort(array):
    for i in range (1, len(array)):
        j = i
        tmp = array[i]
        while (tmp < array[j -1] and j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = tmp

#MERGE SORT
def merge(array, aux, left, mid, right):
    leftIndex = left
    rightIndex = mid + 1
    i = 0
    while ((leftIndex <= mid) and (rightIndex <= right)):
        if array[leftIndex] <= array[rightIndex]:
            aux[i] = array[leftIndex]
            leftIndex += 1
        else:
            aux[i] = array[rightIndex]
            rightIndex += 1
        i += 1
    if leftIndex > mid:
        while rightIndex <= right:
            aux[i] = array[rightIndex]
            i += 1
            rightIndex += 1
    if rightIndex > right:
        while leftIndex <= mid:
            aux[i] = array[leftIndex]
            i += 1
            leftIndex += 1

    for i in range(0,len(array)):
        array[i] = aux[i]

def merge_sort(array, aux, left, right):
    if left < right:
        mid = (left + right) / 2
        merge_sort(array, aux, left, mid)
        merge_sort(array,aux, mid + 1, right)
        merge(array, aux, left, mid, right)

#COUNTING SORT
def counting_sort(array, low, high):
    countLen = high + 1
    count = [0] * countLen;
    for a in array:
        count[a] += 1
    k = 0
    for i in range(countLen):
        for j in range(count[i]):
            array[k] = i
            k += 1
    return array

#SWAP function
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return
