from insertion import insert_sort

def merge_insert_sort(collection):
    length = len(collection)

    if length < 2:
        return collection

    elif length < 21:
        for old_index in range(1, length):
            element = collection[old_index]
            new_index = old_index - 1

            while new_index >= 0 and element < collection[new_index]:
                collection[new_index + 1] = collection[new_index]
                new_index -= 1

            collection[new_index + 1] = element

        return collection

    else:
        midpoint = length // 2
        left_half = merge_insert_sort(collection[:midpoint])
        right_half = merge_insert_sort(collection[midpoint:])

        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection
