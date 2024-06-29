class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = sum(int(digit) for char in s for digit in str(ord(char) - ord('a') + 1))
        for _ in range(k - 1):
            number = sum(int(digit) for digit in str(number))
        
        return number