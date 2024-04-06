class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rmv = []
        for ind, i in enumerate(list(s)):
            if i=="(":
                stack.append(ind)
            elif i == ')' and len(stack)==0:
                rmv.append(ind)
            elif i == ')' and len(stack)>0:
                stack.pop()
        rmv+=stack
        ans = []
        for ind, i in enumerate(list(s)):
            if ind in rmv:
                continue
            else:
                ans.append(i)
        return ''.join(ans)