class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken_set = set(brokenLetters)
        count = 0
        for word in words:
            if not any(letter in broken_set for letter in word):
                count += 1
        return count