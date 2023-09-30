import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(unsorted_list):
    attempts = 0
    while not is_sorted(unsorted_list):
        print(attempts)
        random.shuffle(unsorted_list)
        attempts += 1
        
    return unsorted_list

print(bogo_sort(numbers))
