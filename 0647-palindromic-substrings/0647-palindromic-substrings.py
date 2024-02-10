class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        len_ = len(s)
        self.count = 0
        def dp(i,j):
            if i>j:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==s[j] and dp(i+1, j-1):
                self.count+=1
                memo[(i,j)]=True
                return True
            return False
        for i in range(len_):
            for j in range(i, len_):
                dp(i,j)
        return self.count
                
                