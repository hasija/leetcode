class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        
        if n>=3:
            l1 = s[0]
            l2 = s[1]
            ans = s[:2]
            for i in range(2,n):
                if l1==l2==s[i]:
                    continue
                else:
                    l1, l2 = l2, s[i]
                    ans+=s[i]
        else:
            return s
        return ans
            