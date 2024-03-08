class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        max_ = 0
        for i in nums:
            cnt[i]+=1
            max_ = max(max_, cnt[i])
        
        ans = 0
        for i in cnt.values():
            if i==max_:
                ans+=max_
        return ans
            