class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        n = bin(n)[2:]
        flag = False
        for i in n:
            if flag and i=='1':
                return False
            if i=='1':
                flag = True
        if flag:
            return True
        return False
        