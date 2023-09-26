def linear_search(lst, target):
    """Returns the index position of the target if ounf, else returns None"""

    for n, i in enumerate(lst):
        if i == target:
            return n
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found at list")

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = linear_search(test_list, 12)
verify(result)  # Target not found at list

result = linear_search(test_list, 5)
verify(result)  # Target found at index: 4
