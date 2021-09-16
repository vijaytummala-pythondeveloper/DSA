"""
works only for sorted array
"""


def binary_search(arr, start, end, target):
    mid_index = (start + end) // 2
    if start > end :
        return False
    if target == arr[mid_index]:
        return True

    if target > arr[mid_index]:
        return binary_search(arr, mid_index + 1, end, target)
    else:
        return binary_search(arr, start, mid_index - 1, target)


res = binary_search([10, 20, 30, 40], 0, 3, 10)
print(res)
