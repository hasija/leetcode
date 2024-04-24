class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(num):
            if num in memo:
                return memo[num]
            if num>=3:
                ans = dp(num-1)+dp(num-2)+dp(num-3)
            elif num>0:
                ans = 1
            else:
                ans = 0
            memo[num] = ans
            return memo[num]
        return dp(n)
            