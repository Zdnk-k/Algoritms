#Sorting algoritms written in Python


#INSERTION SORT
def insert_sort(array):
    for i in range (1, len(array)):
        j = i
        tmp = array[i]
        while (tmp < array[j -1] and j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = tmp

#QUICK SORT
def quick_sort_in_place(array, i, j):
    if i < j :
        pivotIndx = j
        leftIndex = i - 1
        for rightIndex in range (i, j + 1):
                if(array[rightIndex] <= array[pivotIndx]):
                    leftIndex += 1
                    swap(array, leftIndex, rightIndex)

        quick_sort_in_place(array, i, leftIndex - 1)
        quick_sort_in_place(array, leftIndex + 1, j)



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

#SELECTION SORT
def minIndex(array, i, j):
    mIndex = i;
    for k in range(i + 1, j):
        if(array[k]) < array[mIndex]:
            mIndex = k
    return mIndex

def select_sort(array):
    for i  in range (0, len(array) - 1):
        mIndex = minIndex(array, i, len(array))
        if (mIndex != array[i]):
            swap(array, i, mIndex)

#BUCKET SORT
def bucket_sort(array, maxElement):
    buckets = []
    for i in range(maxElement / 10 + 2):
        buckets.append([])
    for number in array:
        buckets[number / 10].append(number)
    for bucket in range(len(buckets)):
        quick_sort_in_place(buckets[bucket], 0, len(buckets[bucket]) - 1)
    index = 0
    for  k in range(len(buckets)):
        for number in buckets[k]:
            array[index] = number
            index += 1

#SWAP function
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return
