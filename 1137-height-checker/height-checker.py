class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)  
        counter = 0
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                counter += 1  
        return counter