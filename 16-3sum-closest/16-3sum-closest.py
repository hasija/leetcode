class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        i = 0
        min_sum = float('inf')
        
        if sum(nums[-3:])<target:
            return sum(nums[-3:])
        if sum(nums[:3])>target:
            return sum(nums[:3])
        for i in range(len(nums)-2):
            first = nums[i]
            start,end = i+1, len(nums)-1
            # print (i, min_sum)
            while start<end:
                second=nums[start]
                third=nums[end]
                curr_sum =first+second+third
                if curr_sum==target:
                    return target
                
                if abs(curr_sum-target) <abs(min_sum-target):
                    min_sum = curr_sum
                
                if curr_sum>target:
                    end-=1
                else:
                    start+=1
        return min_sum
                    