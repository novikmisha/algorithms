def insert_sort(collection):
    length = len(collection)

    if length < 2:
        return collection

    for old_index in range(1, length):
        element = collection[old_index]
        new_index = old_index - 1

        while new_index >= 0 and element < collection[new_index]:
            collection[new_index + 1] = collection[new_index]
            new_index -= 1

        collection[new_index + 1] = element

    return collection

 

