from collections import Counter
to_check = input().strip()
char_count = Counter(to_check)
flag_even = 0
flag_odd = 0
for count in char_count.values():
    if count % 2 == 0:
        flag_even = 1  
    else:
        flag_odd = 1  

if flag_odd and flag_even:
    print("0/1")
elif flag_even and flag_odd == 0:
    print("0")
elif flag_odd and flag_even == 0:
    print("1")
