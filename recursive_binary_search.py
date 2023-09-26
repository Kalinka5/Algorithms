def recursive_binary_search(lst, target):
    """Returns the True if target is found, else returns False"""

    if len(lst) == 0:
        return False
    else:
        midpoint = (len(lst)) // 2

        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint+1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)

def verify(index):
    print(f"Target found: {index}")

test_list = [1, 2, 3, 4, 5, 6, 7, 8]

result = recursive_binary_search(test_list, 12)
verify(result)  # Target found: False

result = recursive_binary_search(test_list, 7)
verify(result)  # Target found: True
