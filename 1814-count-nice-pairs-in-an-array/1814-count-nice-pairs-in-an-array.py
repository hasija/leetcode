class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff = defaultdict(int)
        # count = defaultdict(int)
        total = 0
        for i in nums:
            val = i-int(str(i)[::-1])
            diff[val]+=1
            if diff[val]>1:
                # count[val]+=diff[val]-1
                total+=diff[val]-1
        # print (count,diff)
        return total%((10**9)+7)