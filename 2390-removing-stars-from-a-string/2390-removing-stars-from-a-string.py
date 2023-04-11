class Solution:
    def removeStars(self, s: str) -> str:
        ind = 0
        count = 0
        while s:
            # print (ind, len(s))
            if ind>=len(s):
                break
            if s[ind]=='*':
                count+=1
                ind+=1
            else:
                if count:
                    s =  s[:ind-(2*count)]+s[ind:]
                    ind = ind-count*2
                    count=0
                ind+=1
        if count:
            s =  s[:ind-(2*count)]+s[ind:]
        return s
            
                
                    
            
        