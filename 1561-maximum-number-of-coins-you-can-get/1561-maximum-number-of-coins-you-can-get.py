class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        n-=1
        o=0
        val = 0
        while(o<n-1):
            val+=piles[n-1]
            o+=1
            n-=2
        return val