class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        symbols = [(i,x) for i,x in enumerate(dominoes) if x!='.']
        symbols = [(-1, "L")] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols[:-1], symbols[1:]):
            if x==y:
                for ind in range(i+1, j):
                    ans[ind]=x
            elif x>y:
                while i+1<=j-1:
                    i+=1
                    j-=1
                    if i!=j:
                        ans[i]="R"
                        ans[j]="L"
        return "".join(ans)
        