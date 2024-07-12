class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        idx = 1
        max_ = max(x,y)
        min_ = min(x,y)
        ans = 0
        if y>x:
            s=s[::-1]
        cnt = defaultdict(int)
        for i in s:
            if i=='a':
                cnt["a"]+=1
            elif i=='b':
                if cnt['a']>0:
                    cnt['a']-=1
                    ans+=max_
                else:
                    cnt['b']+=1
            else:
                ans+=min(cnt['a'],cnt['b'])*min_
                cnt = defaultdict(int)
        ans+=min(cnt['a'],cnt['b'])*min_
        return ans