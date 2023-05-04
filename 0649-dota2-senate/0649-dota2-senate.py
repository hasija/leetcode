class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        senate = list(senate)
        n = len(senate)
        s = set()
        banned = [False]*n
        ban_r = 0
        ban_d = 0        
        while len(s)!=1:
            s = set()
            for i, val in enumerate(senate):
                if banned[i]:
                    continue
                if val=='D':
                    if ban_d>0:
                        ban_d-=1
                        banned[i]=True
                    else:
                        ban_r+=1
                        s.add('D')
                else:
                    if ban_r>0:
                        ban_r-=1
                        banned[i]=True
                    else:
                        ban_d+=1
                        s.add('R')
        return "Radiant" if s.pop()=='R' else "Dire"
            
        