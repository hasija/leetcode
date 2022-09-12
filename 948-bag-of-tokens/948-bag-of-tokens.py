class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l=0
        r=len(tokens)-1
        score = 0
        tokens = sorted(tokens)
        while (l<=r):
            if power>=tokens[l]:
                score+=1
                power-=tokens[l]
                l+=1
            else:
                if r-l>=1 and score>=1 and tokens[r]+power>=tokens[l]:
                    score-=1
                    power+=tokens[r]
                    r-=1
                else:
                    return score
        return score
    
        