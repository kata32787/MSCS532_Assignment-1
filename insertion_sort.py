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

def main():
    """
    Main function to take user input, sort the array, and print the result.
    """
    # Prompt the user to enter numbers separated by spaces
    arr = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    # Sort the array in descending order
    sorted_arr = insertion_sort_desc(arr)
    # Print the sorted array
    print("Sorted array in descending order:", sorted_arr)

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()

