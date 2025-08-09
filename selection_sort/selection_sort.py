def silly_sort(arr):
    n=len(arr)
    for i in range(n):
        min_lol=i
        for j in range(i,n):
            if arr[min_lol] > arr[j]:
                min_lol= j
        arr[i], arr[min_lol] = arr[min_lol], arr[i]  # swap with i, not j
    return arr


nums=[65,23,34,12,345]
print(silly_sort(nums))
