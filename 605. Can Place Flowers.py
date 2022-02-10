class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last_val = 0
        for x in range(1,len(flowerbed)):
            if flowerbed[x-1] == flowerbed[x] == 0 == last_val:
                flowerbed[x-1] = 1
                n-=1
            last_val = flowerbed[x-1]
            if x == len(flowerbed)-1 and (flowerbed[x-1] == flowerbed[x] == 0):
                n-=1
        if n == len(flowerbed) == 1 and flowerbed[0]==0:
            return True
        if n<=0:
            return True
        else:
            return False
            