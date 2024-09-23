class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}
        n = len(s)
        s_dict = set(dictionary)
        def dp(idx):
            if idx>=n:
                return 0
            if idx in memo:
                return memo[idx]
            # Split at curr_idx
            out = dp(idx+1)+1
            # no split
            char = ""
            for i in range(idx, n):
                char+=s[i]
                if char in s_dict:
                    out = min(dp(i+1), out)
            memo[idx] = out
            return out
        return dp(0)