class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        i = 0
        j = len(s)-1
        flag = True
        elem_repeated = False
        count = collections.Counter(s)
        if len(s)!=len(g):
            return False
        for k,v in count.items():
            if v>1:
                elem_repeated =True
                break
        while i<=j:
            s1=s[i]
            g1 = g[i]
            s2=s[j]
            g2=g[j]

            if s1==g1:
                i+=1
            if s2==g2:
                j-=1
            if s1!=g1 and s2!=g2:
                if s1==g2 and s2==g1 and flag:
                    flag=False
                    i+=1
                    j-=1
                else:
                    return False
        if not flag or elem_repeated:
            return True
        return False
                    
                
