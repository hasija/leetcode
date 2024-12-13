class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = [(i,idx)for idx, i in enumerate(nums)]
        desc = sorted(nums, key = lambda x: (-x[0],-x[1]))
        ans = 0
        marked = set()
        n = len(nums)
        # print(desc)
        while len(marked)!=n:
            i, idx = desc.pop()
            if idx not in marked:
                ans+=i
                marked.add(idx)
                if 0<=idx+1<n:
                    marked.add(idx+1)
                if 0<=idx-1<n:
                    marked.add(idx-1)
                # print(ans, marked)
        return ans