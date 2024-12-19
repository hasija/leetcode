class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_till = 0
        ans = 0
        for idx, i in enumerate(arr):
            max_till = max(i, max_till)
            if idx == max_till:
                ans+=1
        return ans
                