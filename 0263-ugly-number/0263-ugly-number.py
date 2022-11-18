class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        while n!=1:
            if n//2==(n/2):
                n/=2
            elif n//5==(n/5):
                n/=5
            elif n//3==(n/3):
                n/=3
            else:
                return False
        return True