class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        while i<j:
            left = nums[i]
            right = nums[j]
            if left==-right:
                return right
            if abs(left)<abs(right):
                j-=1
            else:
                i+=1
        return -1