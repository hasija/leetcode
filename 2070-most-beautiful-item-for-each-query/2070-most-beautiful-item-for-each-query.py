class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key=lambda x: (x[0],-x[1]))
        last = 0
        price = []
        seen = set()
        beauty = []
        for p,b in items:
            if p in seen:
                continue
            if b>last:
                last = b
            else:
                pass
            beauty.append(last)
            price.append(p)
            
        # print (price, beauty)
        n = len(price)
        ans = []
        for p in queries:
            idx = bisect.bisect_left(price, p)

            if idx>=n or price[idx]!=p:
                idx-=1
            if idx<0:
                ans.append(0)
            else:
                ans.append(beauty[idx])
        return ans