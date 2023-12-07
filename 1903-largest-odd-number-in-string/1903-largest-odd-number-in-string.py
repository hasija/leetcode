class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in reversed(range(n)):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""