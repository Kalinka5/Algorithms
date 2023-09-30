import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def index_of_min(values):
    min_index = 0

    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i

    return min_index


def selection_sort(unsorted_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Takes O(n^2) time
    """
    
    sorted_list = []
    for i in range(len(unsorted_list)):
        index_to_move = index_of_min(unsorted_list)
        sorted_list.append(unsorted_list.pop(index_to_move))
    
    return sorted_list

print(selection_sort(numbers))
