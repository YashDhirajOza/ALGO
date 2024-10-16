t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())  
    arr = list(map(int, input().split()))  
    total_money = 0
    counter = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            if total_money != 0:
                counter += 1  
                total_money -= 1  
        elif arr[i] >= k:
            total_money += arr[i]  
            arr[i] = 0  # Reset the value at arr[i] to 0
    
    print(counter)  
