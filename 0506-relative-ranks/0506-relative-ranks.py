class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [(-i, ind) for ind, i in enumerate(score)]
        arr = sorted(arr, key=lambda x: x[0])
        out = [0]*len(score)
        len_ = len(score)
        for ind, value in enumerate(arr):
            val, o_ind = value
            if ind == 0:
                out[o_ind] = 'Gold Medal'
            elif ind ==1 :
                out[o_ind] = 'Silver Medal'
            elif ind ==2:
                out[o_ind] = 'Bronze Medal'
            else:
                out[o_ind] = str(ind+1)
        return out