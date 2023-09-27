class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        t_len = 0
        for ind,i in enumerate(s):
            if 94>ord(i):
                t_len*=int(i)
            else:
                t_len+=1
            if t_len>=k:
                break
        
        for j in range(ind, -1, -1):
            if ord(s[j])<94:
                t_len/=int(s[j])
                k%=t_len
            else:
                if k==t_len or k==0:
                    return s[j]
                else:
                    t_len-=1
        