class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        offset = 1
        for i in range(1, n+1):
            if offset*2==i:
                offset = i
            ans.append(1+ans[i-offset])
        return ans