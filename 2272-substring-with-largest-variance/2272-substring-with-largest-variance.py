class Solution:
    def largestVariance(self, s: str) -> int:
        n=len(s)
        count=set(s)
        ans=0
        arr=defaultdict(list)
        for i,c in enumerate(s): arr[c].append((i,c))
        for c1 in count:
            for c2 in count:
                if c1!=c2:
                    val,res,m=0,0,10**9+7
                    for _,c in sorted(arr[c1]+arr[c2]):
                        if c==c1: 
                            val+=1
                        elif c==c2:
                            m=min(m,res)
                            val-=1
                            res=val
                        ans=max(ans,val-m)
        return ans
                
            