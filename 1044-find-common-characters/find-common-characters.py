class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        counts = Counter(words[0])
        for word in words[1:]:
            counts &= Counter(word)
        result = []
        for char, count in counts.items():
            result.extend([char] * count)
        return result