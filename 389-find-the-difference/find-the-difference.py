class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        record = list(s)
        for char in t:
            if char in record:
                record.remove(char)
            else:
                return char
        return ''