def insertion_sort(arr):
    for i in range(0, len(arr)):
        index_min = i
        for j in range(i, len(arr)):
            if arr[index_min] > arr[j]:
                index_min = i
        current_min = arr[index_min]
        arr[index_min] = arr[i]
        arr[i] = current_min
            
def selection_sort(arr):
    """Selection sort implemented with a while loop."""
    to_sort = len(arr)
    while to_sort > 1:
        largest = arr[to_sort - 1]
        for j in range(to_sort):
            if arr[j] > largest:
                largest = arr[j]
                index_largest = j
        temp = arr[to_sort]
        arr[to_sort] = largest
        arr[index_largest] = temp
        to_sort -= 1
        
def selection_sort(arr):
    """Selection sort implemented with for loops."""
    to_sort = len(arr)
    for i in range(to_sort-1, 0, -1):
        largest = arr[to_sort - 1]
        for j in range(to_sort):
            if arr[j] > largest:
                largest = arr[j]
                index_largest = j
        temp = arr[to_sort]
        arr[to_sort] = largest
        arr[index_largest] = temp

def merge(arr1, arr2):
    """Merge two arrays."""
    l1 = len(arr1)
    l2 = len(arr2)
    i, j = 0, 0
    result = []
    while i < l1 && j < l2: 
        if arr1[i] >= arr2[j]:
            result.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
    if i > l1:
        k = j
        rem_arr = arr2
        rem_len = l2
    elif j > l2:
        k = i
        rem_arr = arr1
        rem_len = l1
    while k < rem_len:
        result.append(rem_arr[k])
        k += 1
    return result

def recursive_merge_sort(arr):
    arr_len = len(arr)
    left_sorted = recursive_merge_sort(arr[0:arr_len//2])
    right_sorted = recursive_merge_sort(arr[arr_len//2 + 1: arr_len])
    merge(left_sorted, right_sorted)
    
def merge_sort():
    pass

def bubble_sort(arr):
    arr_length = len(arr)
    if arr_length = 1:
        return arr_length
    for i in range(arr_length-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                larger = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = larger
    return arr

def short_bubble_sort(arr):
    if len(arr) == 1 || len(arr) == 0:
        return arr
    is_sorted = True
    i = len(arr) - 1
    while i > 0 and is_sorted == True:
        is_sorted = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                is_sorted = False
                larger = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = larger
        i -= 1
    return arr

def quick_sort():
    pass

# def shell_sort(arr):
#     gap_size = len(arr) // 2
#     while gap_size > 0 :
#         # iterate over all sets of subarrays having at least 2 subarrays
#         for i in range(0, gap_size):
#             # iterate of a set of sub arrays  
        
#         gap_size = gap_size // 2