class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1
        left = True
        while time:
            time-=1
            if idx==n or idx == 1:
                left=not left
            if left:
                idx-=1
            else:
                idx+=1
        return idx
            