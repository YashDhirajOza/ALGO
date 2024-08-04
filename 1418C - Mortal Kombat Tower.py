def count_skip_points(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        ans = 0
        ans += a[0] == 1  # If the first boss is hard, increment ans
        i = 1
        while i < n:
            if a[i] == 0:
                i += 1
                continue
            j = i
            while j < n and a[j] == 1:
                j += 1
            ans += (j - i) // 3
            i = j
        results.append(ans)
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, a))

# Get results
results = count_skip_points(test_cases)

# Print results
for result in results:
    print(result)
