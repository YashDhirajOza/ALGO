class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct_elements = [x for x in arr if count[x] == 1]
        if k > len(distinct_elements):
            return ""
        return distinct_elements[k - 1] ## o based indexing