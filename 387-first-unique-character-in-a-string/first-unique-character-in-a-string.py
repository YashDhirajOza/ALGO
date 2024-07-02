class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx
        return -1  

