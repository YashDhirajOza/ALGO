class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert_to_number(s: str) -> int:
            numeric_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
            return int(numeric_str)
        def sum_of_digits(num: int) -> int:
            return sum(int(digit) for digit in str(num))
        number = convert_to_number(s)
        for _ in range(k):
            number = sum_of_digits(number)
        return number
