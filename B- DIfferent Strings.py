t = int(input())  

for _ in range(t):
    s = input()  
    
    
    if len(set(s)) == 1:
        print("NO")
    else:
        print("YES")

        sorted_str = sorted(s)
        if sorted_str == list(s):
            print(sorted_str[1] + sorted_str[0] + ''.join(sorted_str[2:]))
        else:
            print(''.join(sorted_str))
