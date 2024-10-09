class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in s:
            if i == '(':
                cnt+=1
            else:
                if cnt>0:
                    cnt-=1
                else:
                    ans+=1
        if cnt:
            ans+=cnt
        return ans