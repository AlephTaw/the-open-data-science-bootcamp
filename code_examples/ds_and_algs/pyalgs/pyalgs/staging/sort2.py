"""Sorts"""

def bubble_sort(arr):
    """Bubble sort."""
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    for i in range(arr_length - 1, 0, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def insertion_sort(arr):
    """Insertion sort."""
    for i in range(0, len(arr)):
        index_min = i
        for j in range(i+1, len(arr)):
            if arr[index_min] > arr[j]:
                current_min = arr[j]
                arr[j] = arr[index_min]
                arr[index_min] = current_min
    return arr

def selection_sort(arr):
    """Selection sort."""
    i = len(arr) - 1
    while i > -1:
        largest = arr[i]
        for j in range(i):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        i -= 1
    return arr

def merge(arr1, arr2):
    """Merge."""
    arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
#         print("i: ", arr1[i], "len(arr1):", len(arr1), "j: ", arr2[j], "len(arr2)", len(arr2))
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        elif arr2[j] <= arr1[i]:
            arr.append(arr2[j])
            j += 1
    if i >= len(arr1):
        return arr + arr2[j:]
    else:
        return arr + arr1[i:]

def merge_sort(arr):
    """Merge sort."""
    mid = len(arr)//2
    if mid > 0:
#         print(mid, len(arr) - mid +1)
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        arr = merge(a,b)
#         print('merged')
    return arr