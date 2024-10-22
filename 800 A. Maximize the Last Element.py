t = int(input())  
for _ in range(t):
    n = int(input())  
    arr = list(input().split(' ')) 
    max_answer = 0
    for i in range(0, len(arr), 2):
        max_answer = max(max_answer, arr[i])
    
    print(max_answer)
