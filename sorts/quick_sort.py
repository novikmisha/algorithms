def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right -1
        if right < left:
            done = True
        else:
            myList[right], myList[left] = myList[left], myList[right]

    myList[start], myList[right] = myList[right], myList[start]
    return right

def quicksort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList


if __name__ == "__main__":
    array = [3, 2, 1, 4, 5, 6, 7, 4, 3, 2, 1]
    quicksort(array, 0, len(array) - 1)
    print(array)
