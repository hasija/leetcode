class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [ 0 for val in range(len(s)) ]
        
        if len(s)==1 and s=="0":
            return 0
        if len(s)==1 and s!='0':
            return 1
        
        if s[0]!='0':
            dp[0]=1
        if int(s[:2])>=10 and int(s[:2])<=26:
            dp[1]=1
        if s[1]!='0':
            dp[1]+=dp[0]
        
        for ind in range(2,len(s)):
            curr = s[ind]
            if curr!='0':
                dp[ind] = dp[ind-1]
            if int(s[ind-1:ind+1])>=10 and int(s[ind-1:ind+1])<=26:
                dp[ind]+=dp[ind-2]
        return dp[-1]

                
        
                
        
            
            
            
        