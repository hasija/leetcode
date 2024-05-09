class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        i = 0
        ans = 0
        while i<k:
            val = happiness.pop()
            
            val -=i
            val = max(0, val)
            if val ==0:
                return ans
            ans+=val
            i+=1
        return ans
            