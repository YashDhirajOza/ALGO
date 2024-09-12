t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    alternating_sum = 0
    for i in range(n):
        if i % 2 == 0:  # even index (0-based)
            alternating_sum += a[i]
        else:  # odd index (0-based)
            alternating_sum -= a[i]
    
    print(alternating_sum)
