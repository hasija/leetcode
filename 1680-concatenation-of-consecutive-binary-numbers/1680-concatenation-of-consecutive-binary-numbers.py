class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = format(n, "b")
        out = 0
        new_s = ""
        for ind in range(1,n+1):
            new_s += format(ind, "b")
        # print (new_s)
        # for ind in range(len(new_s)-1, -1, -1):
        #     out+=(2**ind)*int(new_s[ind])
        out = int(new_s, 2)
        return out%(10**9+7)
            
        