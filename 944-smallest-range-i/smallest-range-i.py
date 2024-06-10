class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        adjusted_max = max_val - k
        adjusted_min = min_val + k
        min_score = adjusted_max - adjusted_min
        return max(0, min_score)