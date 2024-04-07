class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        s = list(s)
        def dp(i, stack):
            if (i, stack) in memo:
                return memo[(i, stack)]
            if stack<0:
                return False
            if i>=len(s):
                return stack==0
            if s[i] == '(':
                memo[i, stack] = dp(i+1, stack+1)
            elif s[i] == ')':
                memo[i, stack] = dp(i+1, stack-1)
            else:
                if stack>0 and dp(i+1, stack-1):
                    memo[i, stack] = dp(i+1, stack-1)
                elif dp(i+1, stack+1):
                    memo[i, stack] = dp(i+1, stack+1)
                elif dp(i+1, stack):
                    memo[i, stack] = dp(i+1, stack)
                else:
                    memo[i, stack] = False
            return memo[i, stack]
        return dp(0, 0)
        