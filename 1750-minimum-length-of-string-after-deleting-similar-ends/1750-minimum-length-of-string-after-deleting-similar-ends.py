class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s)-1
        while start<end:
            s1 = s[start]
            s2 = s[end]
            if s1==s2:
                while s[start+1]==s1 and start+1<end:
                    start+=1
                while s[end-1]==s2 and end-1>start:
                    end-=1
                start+=1
                end-=1
            else:
                break
        return end-start+1