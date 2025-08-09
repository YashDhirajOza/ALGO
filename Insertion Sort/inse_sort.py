def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_optimized(arr):
    if len(arr) <= 1:
        return arr, 0, 0  
    arr = arr.copy()  
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Early exit: if key is already in correct position
        if arr[j] <= key:
            comparisons += 1
            continue
        
        # Shift elements and count operations
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            comparisons += 1
            shifts += 1
            j -= 1
        
        arr[j + 1] = key
    
    return arr, comparisons, shifts

def binary_insertion_sort(arr):
    """
    Uses binary search to find insertion point, reducing comparisons
    Time: O(n log n) comparisons, O(n²) shifts
    """
    def binary_search(arr, val, start, end):
        if start == end:
            return start if arr[start] > val else start + 1
        if start > end:
            return start
        mid = (start + end) // 2
        if arr[mid] < val:
            return binary_search(arr, val, mid + 1, end)
        elif arr[mid] > val:
            return binary_search(arr, val, start, mid - 1)
        else:
            return mid
    
    for i in range(1, len(arr)):
        key = arr[i]
        # Find insertion point using binary search
        insertion_pos = binary_search(arr, key, 0, i - 1)
        
        # Shift elements
        for j in range(i, insertion_pos, -1):
            arr[j] = arr[j - 1]
        
        arr[insertion_pos] = key
    
    return arr


numbers = [5, 2, 4, 6, 1, 3]
print("Original array:", numbers)
sorted_array = insertion_sort(numbers.copy())
print("Sorted array:", sorted_array)
