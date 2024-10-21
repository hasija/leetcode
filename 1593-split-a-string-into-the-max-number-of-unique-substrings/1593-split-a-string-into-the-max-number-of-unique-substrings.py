class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        memo = {}
        n = len(s)
        def dp(idx, seen):
            ans = 0
            if idx == n:
                return 0
            for i in range(idx+1, n+1):
                curr = s[idx: i]
                if curr not in seen:
                    seen.add(curr)
                    ans = max(ans, 1+dp(i, seen))
                    seen.remove(curr)
            return ans
        return dp(0, set())