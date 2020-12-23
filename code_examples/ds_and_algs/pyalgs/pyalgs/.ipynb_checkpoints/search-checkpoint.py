def linear_search(arr, value):
    """Linearly search arr for value."""
    i = 0
    while i < len(arr):
        if arr[i] == value:
            return i
    return None

def binary_search(arr, value):
    """Search sorted array with binary search."""
    arr_len = len(arr)
    start = 0
    stop = arr_len - 1
    found = False
    if value < arr[start] || value > arr[stop]:
        return False
    while start <= stop:
        # find midpoint
        mid = (start + stop)//2
        # test
        if value > arr[mid]:
            start = mid + 1
        elif value < arr[mid]:
            stop = mid - 1
        elif value == arr[mid]:
            return mid
    return False