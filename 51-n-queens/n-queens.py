import itertools as it
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_solution(perm):
            for (i1, i2) in it.combinations(range(len(perm)), 2):
                if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
                    return False
            return True
        
        solutions = []
        
        for perm in it.permutations(range(n)):
            if is_solution(perm):
                board = []
                for row in perm:
                    board.append('.' * row + 'Q' + '.' * (n - row - 1))
                solutions.append(board)
        
        return solutions