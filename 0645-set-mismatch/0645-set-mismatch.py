class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = len(nums)
        repeat = None
        missing = None
        for i in range(total):
            curr = abs(nums[i])
            if nums[curr-1]<0:
                repeat = curr
            else:
                nums[curr-1]*=-1
        for i in range(total):
            if nums[i]>0:
                missing = i+1
        return [repeat, missing]