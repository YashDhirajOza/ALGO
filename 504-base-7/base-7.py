class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        
        base7_digits = []
        while num > 0:
            base7_digits.append(str(num % 7))
            num //= 7
        
        if negative:
            base7_digits.append('-')
        
        return ''.join(base7_digits[::-1])
        