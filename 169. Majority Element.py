class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = None
        for x in nums:
            if curr is None:
                curr=x
                count=1
                continue
            else:
                if curr==x:
                    count+=1
                elif count==1:
                    curr=x
                else:
                    count-=1
        return curr
                