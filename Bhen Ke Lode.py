t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split())) 
    sum_even = -1
    sum_odd = -1
    counter_even = 0
    counter_odd = 0
    
    for i in range(n):
        if i % 2 == 0: 
            counter_even += 1
            sum_even = max(sum_even, arr[i])
        else: 
            counter_odd += 1
            sum_odd = max(sum_odd, arr[i])
    
    answer = max(sum_even, sum_odd)
    if answer == sum_even:
        print(answer + counter_even)
    else:
        print(answer + counter_odd)
