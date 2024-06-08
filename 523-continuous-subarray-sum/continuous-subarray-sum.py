class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums) - 1))
        remainder_dict = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                remainder_dict[remainder] = i

        return False
