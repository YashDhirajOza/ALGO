class Solution:
    def scoreOfString(self, s: str) -> int:
        total_sum = 0
        for i in range(1, len(s)):
            diff = abs(ord(s[i]) - ord(s[i - 1]))
            total_sum += diff
        return total_sum