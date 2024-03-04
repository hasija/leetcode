class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens)-1
        score = 0
        max_ = 0
        while start<=end:
            curr = tokens[start]
            if curr<=power:
                power-=curr
                score+=1
                max_ = max(score, max_)
                start+=1
            elif score>0:
                score-=1
                power+=tokens[end]
                end-=1
            else:
                break
        return max_
            