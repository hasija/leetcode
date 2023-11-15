class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for ind, i in enumerate(arr):
            if ind==0:
                prev=1
                continue
            if i-prev<=1:
                prev=i
            else:
                prev=prev+1
        return prev