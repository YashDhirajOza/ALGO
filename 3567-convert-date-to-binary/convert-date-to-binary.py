class Solution:
    def decimal_to_binary(self, n):    
        if n == 0:
            return "0"
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary  
            n //= 2  
        return binary

    def convertDateToBinary(self, date: str) -> str:
        year, mth, day = map(int, date.split('-'))  
        year_new = self.decimal_to_binary(year)  
        mth_new = self.decimal_to_binary(mth)
        day_new = self.decimal_to_binary(day)
        answer= year_new +"-"+ mth_new +"-"+ day_new
        return answer