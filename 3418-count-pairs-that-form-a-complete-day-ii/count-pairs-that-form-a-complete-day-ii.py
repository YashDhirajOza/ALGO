class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = {}
        count_pairs = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24  
            
            if complement in remainder_count:
                count_pairs += remainder_count[complement]
            
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count_pairs

