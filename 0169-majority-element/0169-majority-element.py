class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        prev = None
        for i in nums:
            if prev!=i:
                count -= 1
                if count ==0:
                    prev = i
                    count = 1
            else:
                count+=1
        return prev
            
        