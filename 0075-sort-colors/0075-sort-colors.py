class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        h = len(nums)-1
        while m<=h:
            curr = nums[m]
            if curr == 0:
                nums[l], nums[m],=nums[m], nums[l]
                if l==m:
                    m+=1
                l+=1
            elif curr == 1:
                m+=1
            else:
                nums[h], nums[m],=nums[m], nums[h]
                h-=1
            # print (nums, l,m,h)
        return nums
                
            
                
        