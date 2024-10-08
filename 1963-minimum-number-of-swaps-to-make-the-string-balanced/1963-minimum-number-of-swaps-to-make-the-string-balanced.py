class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        p1 = 0
        p2 = n-1
        cnt_open = 0
        ans = 0
        while p1<p2:
            if s[p1]==']':
                cnt_open-=1
            else:
                cnt_open+=1
            p1+=1
            if cnt_open<0:
                while p2>p1 and s[p2]!='[':
                    p2-=1
                ans+=1
                cnt_open = 1
        return ans
            