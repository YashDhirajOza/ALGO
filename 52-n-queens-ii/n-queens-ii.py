class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_be_extended_to_solution(perm):
            i = len(perm) - 1
            for j in range(i):
                if i - j == abs(perm[i] - perm[j]):
                    return False
            return True
        
        def extend(perm, n, count):
            if len(perm) == n:
                count[0] += 1
                return
            
            for k in range(n):
                if k not in perm:
                    perm.append(k)
                    if can_be_extended_to_solution(perm):
                        extend(perm, n, count)
                    perm.pop()

        count = [0]
        extend([], n, count)
        return count[0]

