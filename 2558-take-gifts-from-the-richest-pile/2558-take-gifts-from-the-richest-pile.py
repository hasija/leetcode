class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts  = [-val for val in gifts]
        heapq.heapify(gifts)
        while k:
            val = heapq.heappop(gifts)
            val = int(math.sqrt(val*-1))
            heapq.heappush(gifts, val*-1)
            k-=1
        return sum([-val for val in gifts])
