# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the value of n
    n = int(input())
    
    # Calculate the remainder when n is divided by 5
    remainder = n % 5
    
    # Check the remainder to determine the minimum number of 1-burle coins needed
    if remainder == 0:
        # If remainder is 0, no 1-burle coins needed
        print(0)
    elif remainder <= 2:
        # If remainder is 1 or 2, use one 1-burle coin
        print(1)
    else:
        # If remainder is 3 or 4, use two 1-burle coins
        print(2)
