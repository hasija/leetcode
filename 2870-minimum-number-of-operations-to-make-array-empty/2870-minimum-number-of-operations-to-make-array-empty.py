class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for i,j in cnt.items():
            if j == 1:
                return -1
            if j%3==0:
                ans+=j//3
            else:
                ans+=j//3+1
        return ans
                