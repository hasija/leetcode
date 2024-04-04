class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        max_ = 0
        for i in s:
            if i == "(":
                stack+=1
                max_ = max(stack, max_)
            elif i == ')':
                stack-=1
        return max_