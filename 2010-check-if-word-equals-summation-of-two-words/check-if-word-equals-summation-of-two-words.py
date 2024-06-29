class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word: str) -> int:
            letter_to_index = {chr(i): i - 97 for i in range(97, 123)}
            return int(''.join(str(letter_to_index[char]) for char in word))
        word_1 = convert(firstWord)
        word_2 = convert(secondWord)
        target = convert(targetWord)
        return word_1 + word_2 == target
