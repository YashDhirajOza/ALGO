class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        result = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                result.append(num)
        nums[:] = result
        return len(result)
 ## set does not keep the order as it is this question required th keep thre order same
 