class Solution:
    def __init__(self):
        self.d = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

    def extract_digits(self, num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.reverse()
        return digits

    def naming(self, num):
        if num < 20:
            return self.d[num]
        elif num < 100:
            tens = num // 10 * 10
            ones = num % 10
            return self.d[tens] + ('' if ones == 0 else ' ' + self.d[ones])
        elif num < 1000:
            hundreds = num // 100
            remainder = num % 100
            return self.d[hundreds] + ' Hundred' + ('' if remainder == 0 else ' ' + self.naming(remainder))
        elif num < 1000000:
            thousands = num // 1000
            remainder = num % 1000
            return self.naming(thousands) + ' Thousand' + ('' if remainder == 0 else ' ' + self.naming(remainder))
        elif num < 1000000000:
            millions = num // 1000000
            remainder = num % 1000000
            return self.naming(millions) + ' Million' + ('' if remainder == 0 else ' ' + self.naming(remainder))
        elif num < 1000000000000:
            billions = num // 1000000000
            remainder = num % 1000000000
            return self.naming(billions) + ' Billion' + ('' if remainder == 0 else ' ' + self.naming(remainder))
        else:
            raise ValueError("Number too large to handle")

    def convert_to_words(self, num):
        return self.naming(num)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.d[num]
        return self.convert_to_words(num)

