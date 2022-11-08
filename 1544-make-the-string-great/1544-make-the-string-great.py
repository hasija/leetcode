class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        n = len(s)
        while (i<n): 
            if i==0:
                i+=1
                continue
            curr = s[i]
            past = s[i-1]
            if curr!=past and (curr.lower()==past or curr==past.lower()):
                s=s[:i-1]+s[i+1:]
                n = len(s)
                i-=1
            else:
                i+=1
        return s
                