class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        len_ = len(s)
        ones = sum([1 for i in s if i=='1'])-1
        out = ""
        for i in range(ones):
            out+="1"
        for i in range(ones, len_-1):
            out+="0"
        out+="1"
        return out
        