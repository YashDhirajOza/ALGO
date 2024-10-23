class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        min_average = float('inf')
        left, right = 0, n - 1
        for _ in range(n // 2):
            average = (nums[left] + nums[right]) / 2.0
            min_average = min(min_average, average)
            left += 1
            right -= 1
        return min_average
        #[1,4,4,7,8,13,15]