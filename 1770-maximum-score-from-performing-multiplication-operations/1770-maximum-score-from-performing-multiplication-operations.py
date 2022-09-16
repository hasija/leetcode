class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0]*(m+1) for i in range(m+1)]
        
        for op in range(m-1, -1,-1):
            for left in range(op,-1,-1):
                right = (n-1-(op-left))
                dp[op][left] = max(
                                    (nums[left]*multipliers[op])+dp[op+1][left+1],
                                    (nums[right]*multipliers[op])+dp[op+1][left]
                )
        return dp[0][0]
            