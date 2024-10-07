class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        i=0
        to_find = set(["AB","CD"])
        stack = []
        while i<n:
            if not stack:
                stack.append(s[i])
                i+=1
                continue
            if stack[-1]+s[i] in to_find:
                stack.pop()
                i+=1
            else:
                stack.append(s[i])
                i+=1
        return len(stack)
                
            