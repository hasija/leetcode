from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=r=0
        out = 0
        for ind in range(len(s)):
            r+=1
            count[s[ind]] = count.get(s[ind],0)+1
            max_val = sorted(count.items(), key=lambda x: -x[1])[0][1]
            if r-l-max_val<=k and out < r-l:
                out=r-l
            elif r-l-max_val>k:
                count[s[l]]-=1
                l+=1
        # print (out)
        return out
                
            
        