class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        min_idx = 0
        start = 0
        n = len(prices)
        ans = []
        for idx, i in enumerate(prices):
            while min_idx == idx or prices[min_idx]>prices[idx]:
                min_idx+=1
                if min_idx>=n:
                    ans.append(i)
                    min_idx = idx+1
                    break
            else:
                ans.append(i-prices[min_idx])
                min_idx = idx+1
        return ans