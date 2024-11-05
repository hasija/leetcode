class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(0,n,2):
            p1 = s[i]
            p2 = s[i+1]
            if p1==p2:
                continue
            else:
                cnt+=1
        return cnt