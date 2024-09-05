class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_ = sum(rolls)
        len_ = len(rolls)+n
        val=(mean*len_)-sum_
        ans = []
        if val<=6*n and val>=n:
            for i in range(n):
                to_take = val-(n-i-1)
                if to_take<=6:
                    pass
                else:
                    to_take = 6
                ans.append(to_take)
                val-=to_take
                # Case 1: val is less than 6 and n is higher
                # case 2: val is very large and n is small
        return ans