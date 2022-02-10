class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums[abs(nums[x])-1]=abs(nums[abs(nums[x])-1])*-1
        return [x+1 for x in range(len(nums)) if nums[x]>0]