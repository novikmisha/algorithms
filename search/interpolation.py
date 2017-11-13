def interpolation_search(array, item):
    min = 0
    max = len(array) - 1

    k = 0

    while min <= max and array[min] <= item <= array[max]:
        k+=1
        middle = min + ((item - array[min]) * (max - min)) // (array[max] - array[min])
        if array[middle] < item:
            min = middle + 1
        elif array[middle] > item:
            max = middle - 1
        else:
            return middle, k

    return -1, k
