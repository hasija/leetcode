class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n =  len(nums)
        if n<=4:
            return 0
        
        l = 0
        r = n-1
        moves = 0
        ans = float('inf')
        for i in range(4):
            l = i
            r = n-(4-l)
            diff = nums[r]-nums[l]
            ans = min(diff, ans)
        return ans
            
        