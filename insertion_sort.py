def insertion_sort_desc(arr):
    """
    Perform an insertion sort to sort the array in descending order.
    :param arr: List of numbers to be sorted
    :return: Sorted list in descending order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
