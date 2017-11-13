def binary_search(array, item):
    min = 0
    max = len(array) - 1

    k = 0

    while min <= max:
        k+=1
        middle = (min + max) // 2
        if array[middle] < item:
            min = middle + 1
        elif array[middle] > item:
            max = middle - 1
        else:
            return middle, k

    return -1, k
