#

t = int(input())
def con_1(n):
    return n>=2 ## would if reutrn if length of the string in less then 2 
## condition for good string length>=2
def con_3(start,end):
    return start!=end ## would return if the first and last element are not same  
# condition for first and last element must not be same 
def con_2(arr):
    
    
    
for _ in range(t):
    n = 2  # Number of strings to be input
    arr = [input() for _ in range(n)]  # List comprehension to take 'n' inputs
    if (con_1 and con_2 and con_3):
        print("Yes")
    else:
        print("N0")

