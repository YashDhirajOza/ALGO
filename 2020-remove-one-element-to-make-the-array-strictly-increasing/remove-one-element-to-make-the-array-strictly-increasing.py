class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                counter += 1
                if counter > 1:
                    return False
                if i == 1 or nums[i] > nums[i - 2]:
                    continue
                elif i == len(nums) - 1 or nums[i + 1] > nums[i - 1]:
                    continue
                else:
                    return False
        return True
