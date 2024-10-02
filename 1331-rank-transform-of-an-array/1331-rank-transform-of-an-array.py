class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = arr.copy()
        arr.sort()
        rank = {}
        cnt = 1
        for i in arr:
            if i in rank:
                continue
            else:
                rank[i]=cnt
                cnt+=1
        out = []
        for i in new_arr:
            out.append(rank[i])
        return out
        