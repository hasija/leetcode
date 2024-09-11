class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = list(reversed(bin(start)[2:]))
        goal = list(reversed(bin(goal)[2:]))
        ans = 0
        for idx in range(max(len(goal), len(start))):
            try:
                first = goal[idx]
            except:
                first = '0'
            try:
                second = start[idx]
            except:
                second = '0'
            
            
            if first!=second:
                ans+=1
        return ans
        
        