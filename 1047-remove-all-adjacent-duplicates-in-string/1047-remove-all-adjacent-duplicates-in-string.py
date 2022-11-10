class Solution:
    def removeDuplicates(self, s: str) -> str:
        ind = 0
        while ind <len(s):
            if ind==0:
                ind+=1
                continue
            if s[ind-1] == s[ind]:
                s = s[:ind-1]+s[ind+1:]
                ind-=1
            else:
                ind+=1
        return s
            