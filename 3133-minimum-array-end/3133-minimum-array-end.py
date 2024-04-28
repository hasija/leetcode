class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x_bits = bin(x)[2:]
        if n==1:
            return x
        # number to find
        new_n = n-1
        new_n = bin(new_n)[2:]
        new_n = list(reversed(new_n))
        cnt = 0
        ans = ""
        for i in reversed(x_bits):
            if i=='0' and  cnt<len(new_n):
                ans = new_n[cnt]+ans
                cnt+=1
            else:
                ans = i+ans
        # print ("def" ,ans)
        # print ("rem", ''.join(new_n[cnt:]))
        new_n = reversed(new_n[cnt:])
        ans = ''.join(new_n)+ans
        
        # print(ans)
        return int(ans,2)