class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        for x in range(len(nums)):
            # print (f"values: {right},{left}")
            mid = ((right-left)//2)+left
            # print (f"value of mid:{nums[mid]}")
            if nums[mid]==target:
                return mid
            if left>=right:
                break
            if nums[mid]>target and nums[left]<=target:
                # print ("1st")
                move = "left"
                right = mid-1
            elif nums[mid]<target and nums[right]>=target:
                # print ("2nd")
                move="right"
                left = mid+1
            elif nums[mid]<target and nums[right]<target and nums[mid]<nums[right]:
                # print ("3rd")
                move = "left"
                right = mid-1
            elif nums[mid]>target and nums[left]>target and nums[left]<nums[mid]:
                # print ("4th")
                move="right"
                left = mid+1
            elif nums[mid]<target and nums[right]<target and nums[mid]>=nums[right]:
                # print ("5th")
                move="right"
                left = mid+1
            elif nums[mid]>target and nums[left]>target and nums[left]<=nums[mid]:
                # print ("6th")
                move = "right"
                left = mid+1
            elif nums[left]>target and nums[mid]>target and nums[mid]<nums[left]:
                # print ("7th")
                move="left"
                right = mid-1
                
            else:
                move="none"
                pass
            # print (move)
            if right>=len(nums) or right<0 or left<0 or left>=len(nums):
                break
            
        return -1