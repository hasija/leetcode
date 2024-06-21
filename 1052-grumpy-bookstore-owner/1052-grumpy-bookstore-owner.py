class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grump_score = []
        last_score = 0
        base_score = 0
        for idx, i in enumerate(customers):
            if grumpy[idx]!=1:
                base_score +=i
                grump_score.append(last_score)
            else:
                last_score += i
                grump_score.append(last_score)
                
        
        max_g = 0
        # print (grump_score)
        for i in range(minutes-1, len(grump_score)):
            if i-minutes>=0:
                final = grump_score[i]-grump_score[i-minutes]
            else:
                final = grump_score[i]
            max_g = max(max_g, final)
        # print (base_score, max_g)
        return max_g+base_score
            
                