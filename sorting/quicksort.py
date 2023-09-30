import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def quicksort(unsorted_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Worst case - O(n^2) time; Best case - O(n log n) time
    """

    if len(unsorted_list) <= 1:
        return unsorted_list
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = unsorted_list[0]

    for value in unsorted_list[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
