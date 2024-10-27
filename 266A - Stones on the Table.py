n= int(input())
arr=list(input())
flag=True
for i in range(1,n):
    if arr[i-1] != arr[i]:
        print(i-1)
        flag=False
        break
if flag:
    print(n-1)
    
    
        
    
    
