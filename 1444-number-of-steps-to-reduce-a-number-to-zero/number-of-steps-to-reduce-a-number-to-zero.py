class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        n = num
        while n != 0:
            n = n // 2 if n % 2 == 0 else n - 1
            counter += 1
        return counter
