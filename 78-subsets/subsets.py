class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        n = len(nums)
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if i & (1 << j):  # Check if the j-th bit is set
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets

