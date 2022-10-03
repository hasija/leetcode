class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = None
        prev_val = 0
        same_flag = False
        total_time = 0
        for ind in range(len(colors)):
            if prev is None:
                prev = colors[ind]
                prev_val = neededTime[ind]
                continue
            curr = colors[ind]
            if prev == curr:
                total_time += min(neededTime[ind], prev_val)
                prev_val = max(neededTime[ind], prev_val)
            else:
               
                prev = colors[ind]
                prev_val = neededTime[ind]
       
        return total_time