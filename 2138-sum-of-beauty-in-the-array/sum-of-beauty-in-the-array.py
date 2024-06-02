class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        beauty_sum = 0
        
        left_max = [0] * n
        right_min = [0] * n
        
        left_max[0] = nums[0]
        right_min[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
        
        for i in range(1, n - 1):
            if left_max[i - 1] < nums[i] < right_min[i + 1]:
                beauty_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty_sum += 1
        
        return beauty_sum

