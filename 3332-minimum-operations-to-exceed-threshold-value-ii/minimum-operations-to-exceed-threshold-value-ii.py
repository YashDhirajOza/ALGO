class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while nums and nums[0] < k:
            min_1 = heappop(nums)
            if not nums:
                break
            min_2 = heappop(nums)
            heappush(nums, min_1*2 + min_2)
            operations += 1
        return operations if all(num >= k for num in nums) else -1

