class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        s = list(s)
        # print (s)
        while len(s)>1 and i<len(s):
            if i==0:
                i+=1
                continue
            if s[i].lower()==s[i-1].lower() and ord(s[i])!=ord(s[i-1]):
                del s[i]
                del s[i-1]
                # print (i, s)
                i-=1
                continue
            else:
                i+=1
        return ''.join(s)