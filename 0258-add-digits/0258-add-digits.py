class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            tmp = str(num)
            num = sum([int(i) for i in list(tmp)])
        return num