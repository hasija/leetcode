class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        out = -1
        i=j=lenv=0
        t_sum = sum(nums)-x
        sumv=0
        while j<n:
            sumv +=nums[j]
            lenv +=1
            while sumv>t_sum and i<=j:
                sumv-=nums[i]
                i+=1
                lenv-=1
            if sumv==t_sum:
                out = max(out, lenv)
            j+=1
        return  -1 if out==-1 else n-out
                