class Solution:
    def strangePrinter(self, s: str) -> int:
        s = ''.join([char for char, _ in groupby(s)])
        
        memo = {}
        
        def dp(start, end):
            if start>end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            
            worst_case = 1+ dp(start+1, end)
            
            for i in range(start+1, end+1):
                if s[i]==s[start]:
                    worst_case = min(dp(start, i-1)+dp(i+1, end), worst_case)
            memo[(start,end)] = worst_case
            return worst_case
        return dp(0, len(s)-1)