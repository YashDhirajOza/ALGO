n = int(input())
arr = list(map(int, input().split()))
counter = 0
for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
        diff = arr[i-1] - arr[i]
        arr[i] = arr[i-1]
        counter += diff
print(counter)
