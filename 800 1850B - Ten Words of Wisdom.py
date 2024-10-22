t = int(input())  

for _ in range(t):
    n = int(input())  
    best_index = -1
    best_quality = -1

    for i in range(1, n + 1):
        a, b = map(int, input().split())  
        if a <= 10:
            if b > best_quality:
                best_quality = b
                best_index = i
    
    print(best_index)
