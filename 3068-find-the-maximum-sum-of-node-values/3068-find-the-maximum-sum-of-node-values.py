class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = {}
        
        def dp(n, zor):
            if n == len(nums):
                if zor:
                    return -float('inf')
                else:
                    return 0
            if (n, zor) in memo:
                return memo[(n,zor)]
            w_xor = (nums[n]^k)+ dp(n+1, not zor)
            wo_xor = nums[n]+dp(n+1, zor)
            val = max(w_xor, wo_xor)
            memo[(n,zor)] = val
            return memo[(n,zor)]
        return dp(0, False)
                