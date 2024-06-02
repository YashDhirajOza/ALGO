class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        num_bits = num.bit_length()
        return num_bits + bin(num).count('1') - 1