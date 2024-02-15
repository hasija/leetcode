class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        len_ = len(nums)
        for i in range(len_-1, 1, -1):
            curr = nums[i]
            total-=curr
            # print ("totalm curr", total, curr)
            if total>curr:
                return total+curr
        return -1
        