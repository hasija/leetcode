class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        memo = {}
        
        def action(operator,a,b):
            if operator == '+':
                return a+b
            elif operator == '-':
                return a-b
            else:
                return a*b
        
        def dp(exp):
            n = len(exp)
            if n==1:
                return [int(exp)]
            if n==2 and exp[0].isdigit():
                return [int(exp)]
            ans = []
            for i, char in enumerate(exp):
                if char in "+-*":
                    # Divide the exp and cal both sides
                    left = dp(exp[:i])
                    right = dp(exp[i+1:])
                    for l in left:
                        for r in right:
                            ans.append(action(char, l, r))
            return ans
        return dp(exp)
                    