class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = curr = 0
        flag = False
        max_c = 0
        for i in nums:
            if i==1:
                curr+=1
            else:
                flag=True
                max_c = max(prev+curr, max_c)
                prev = curr
                curr = 0

        max_c = max(prev+curr, max_c)
        if not flag:
            max_c-=1
        return max_c