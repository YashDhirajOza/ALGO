class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        n = len(nums)
        nums = deque(nums)
        
        for _ in range(n // 2):
            minElement = nums.popleft()
            maxElement = nums.pop()
            average = (minElement + maxElement) / 2
            averages.append(average)
        
        return min(averages)