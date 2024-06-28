import itertools as it
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_be_extended_to_solution(perm):
            i = len(perm) - 1
            for j in range(i):
                if i - j == abs(perm[i] - perm[j]):
                    return False
            return True
        
        def extend(perm, n):
            if len(perm) == n:
                board = []
                for row in perm:
                    board.append('.' * row + 'Q' + '.' * (n - row - 1))
                solutions.append(board)
                return
            
            for k in range(n):
                if k not in perm:
                    perm.append(k)
                    if can_be_extended_to_solution(perm):
                        extend(perm, n)
                    perm.pop()
        
        solutions = []
        extend([], n)
        
        return solutions