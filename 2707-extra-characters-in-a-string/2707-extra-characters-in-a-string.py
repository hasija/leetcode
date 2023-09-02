class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        end = len(s)
        w_set = set(dictionary)
        memo = defaultdict(int)
        def dp(start):
            if start in memo:
                return memo[start]
            if start == end:
                return 0
            # skip curr char
            ans = dp(start+1)+1
            
            for i in range(start, end):
                word = s[start:i+1]
                if word in w_set:
                    ans = min(ans, dp(i+1))
            memo[start] = ans
            return ans
        return dp(0)
                
            