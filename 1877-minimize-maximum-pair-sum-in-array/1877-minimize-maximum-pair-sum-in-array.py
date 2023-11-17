class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        j = n-1
        max_one = 0
        for i in range(n//2):
            max_one = max(max_one, nums[i]+nums[j])
            j-=1
        return max_one
        