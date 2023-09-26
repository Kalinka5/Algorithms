def binary_search(lst, target):
    """Returns the index position of the target if found, else returns None"""
    
    start = 0
    end = len(lst) - 1

    while start <= end:
        midpoint = (start + end) // 2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            start = midpoint + 1
        else:
            end = midpoint - 1 
    
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found at list")

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = binary_search(test_list, 12)
verify(result)  # Target not found at list

result = binary_search(test_list, 5)
verify(result)  # Target found at index: 4
