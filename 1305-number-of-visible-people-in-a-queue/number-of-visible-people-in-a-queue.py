class Solution:
    def canSeePersonsCount(self, arr: List[int]) -> List[int]:
        stack = []
        soln = [0] * len(arr)
        cnt = 0
        
        for i in range(len(arr) - 1, -1, -1):
            if not stack:
                stack.append(arr[i])
                soln[i] = 0
            else:
                while stack and stack[-1] < arr[i]:
                    cnt += 1
                    stack.pop()
                
                if cnt == 0:
                    soln[i] = 1
                elif stack:
                    soln[i] = cnt + 1
                else:
                    soln[i] = cnt
                
                stack.append(arr[i])
                cnt = 0
        
        return soln
