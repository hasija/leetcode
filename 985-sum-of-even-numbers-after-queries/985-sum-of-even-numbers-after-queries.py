class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = []
        
        even = 0
        for n_val in nums:
            if n_val%2==0:
                even+=n_val
        
        
        for ind in range(len(nums)):
            val, q_ind = queries[ind]
            if nums[q_ind]%2==0:
                even-=nums[q_ind]
            nums[q_ind]+=val
            if nums[q_ind]%2==0:
                even+=nums[q_ind]
            
            
            ret.append(even)
        return ret
                
        