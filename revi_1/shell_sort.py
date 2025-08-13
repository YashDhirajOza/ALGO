def shell_sort(arr):
    n = len(arr)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2  # Reduce the gap
    return arr

# Example usage
example = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(example))  # Output: [11, 12, 22, 25, 34, 64, 90]
