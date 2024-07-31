class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        answer = 1  
        for i in range(1, n):
            answer += i * 4  
        return answer
