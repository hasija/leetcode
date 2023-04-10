class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','{':'}', '[':']'}
        for v in s:
            if v in dic:
                stack.append(dic[v])
            else:
                if stack and  v==stack.pop():
                    continue
                else:
                    return False
        if stack:
            return False
        return True
        