class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        start = False
        out = [-1]*n
        count = k+k+1
        for idx in range(k,n-k):
            if not start:
                total = sum(nums[:idx+k+1])
                s = nums[0]
                out[idx] = total//count
                start = True
            else:
                total-=s
                total+=nums[idx+k]
                s = nums[idx-k]
                out[idx] = total//count
        return out