class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        
        for w,l in matches:
            if w not in lost:
                lost[w]=0
            if l not in lost:
                lost[l]=1
            else:
                lost[l]+=1
        win = []
        loss = []
        for k,v in lost.items():
            if v==0:
                win.append(k)
            if v==1:
                loss.append(k)
        win = sorted(win)
        loss = sorted(loss)
        return [win, loss]