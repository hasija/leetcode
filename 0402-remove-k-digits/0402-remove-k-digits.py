class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and i<stack[-1] and k>0:
                stack.pop()
                k-=1
            if stack or i!='0':
                stack.append(i)
        
        if k>0:
            stack = stack[:-k]
        
        return ''.join(stack) or '0'