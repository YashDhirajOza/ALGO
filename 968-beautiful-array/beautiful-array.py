class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def construct_beautiful_array(nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums
            odd = construct_beautiful_array(nums[::2])
            even = construct_beautiful_array(nums[1::2])
            return odd + even
        
        return construct_beautiful_array(list(range(1, n + 1)))
