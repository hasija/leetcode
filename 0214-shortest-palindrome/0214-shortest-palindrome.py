class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        for i in range(n):
            if s[:n-i]!=rev_s[i:]:
                continue
            else:
                # print(rev_s[:i], 'matched part',s[:n-i], 'non matched',s[n-i:])
                return rev_s[:i]+s[:n-i]+s[n-i:]
        return ""