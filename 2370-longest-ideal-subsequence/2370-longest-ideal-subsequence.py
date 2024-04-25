class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        memo = [[-1]*27 for i in s]
        def dp(ind, last):
            if ind>=len(s):
                return 0
            if last is not None:
                last_ind = ord(last)-97
            else:
                last_ind = 26
            # print (ind, last_ind)
            if memo[ind][last_ind] != -1:
                return memo[ind][last_ind]

            ans1 = 0
            
            if last is not None and abs(ord(s[ind])-ord(last))<=k:
                ans1 = dp(ind+1, s[ind])+1
            elif last is None:
                ans1 = dp(ind+1, s[ind])+1
            ans2 = dp(ind+1, last)

            if ans1>ans2:
                memo[ind][last_ind] = ans1
            else:
                memo[ind][last_ind] = ans2
            return memo[ind][last_ind]
            
        return dp(0, None)
                