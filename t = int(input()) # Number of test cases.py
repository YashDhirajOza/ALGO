t = int(input())  # Number of test cases

for _ in range(t):
    s = input()  # Read the binary string for the current test case
    
    # If the string is already sorted, only one piece is needed
    if s == ''.join(sorted(s)):
        print(1)
        continue
    
    pieces = 0
    prev = '0'
    
    # Count the number of segments where 1 appears after 0
    for digit in s:
        if digit == '1' and prev == '0':
            pieces += 1
        prev = digit
    
    print(pieces + 1)  # Add 1 for the last segment
