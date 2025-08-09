def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def bubble_sort_optimized(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Flag to track if any swap occurred
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is already sorted
        if not swapped:
            break
    
    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)
sorted_array = bubble_sort(numbers.copy())  # Use copy to preserve original
print("Sorted array:", sorted_array)
