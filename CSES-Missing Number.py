n = int(input())
arr = list(map(int, input().split()))
arr.sort()

missing_number = None
for i in range(len(arr)):
    if i + 1 != arr[i]:
        missing_number = i + 1
        break

if missing_number is None:
    missing_number = len(arr) + 1

print(missing_number)

