from collections import Counter

def find_palindrome(s):
    count = Counter(s)
    odd_count = 0
    odd_char = ""
    
    # Check for characters with odd frequencies
    for char, freq in count.items():
        if freq % 2 != 0:
            odd_count += 1
            odd_char = char
        if odd_count > 1:
            return "NO SOLUTION"
    
    # Form the first half of the palindrome
    first_half = []
    for char, freq in count.items():
        first_half.append(char * (freq // 2))
    
    # Form the full palindrome
    first_half = ''.join(first_half)
    second_half = first_half[::-1]
    if odd_count == 1:
        return first_half + odd_char + second_half
    else:
        return first_half + second_half

# Input reading
s = input().strip()
# Output the result
print(find_palindrome(s))
