class Solution:
    def decimal_to_binary(self, n):
        if n == 0:
            return "0"
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary  
            n //= 2  
        return binary

    def hammingWeight(self, n: int) -> int:
        answer = self.decimal_to_binary(n)
        counter = 0
        for i in range(len(answer)):
            if answer[i] == '1':  
                counter += 1
                
        return counter