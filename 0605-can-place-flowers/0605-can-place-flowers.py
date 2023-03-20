class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free = False
        if len(flowerbed)==1 and n==1 and flowerbed[0]==0:
            return True
        max_l = len(flowerbed)
        for ind, val in enumerate(flowerbed):
            prev=0
            if ind>0:
                prev = flowerbed[ind-1]
            next = 0
            if ind+1<max_l:
                next = flowerbed[ind+1]
            if val==0 and prev==0 and next==0:
                n-=1
                flowerbed[ind]=1
            
        if n<=0:
            return True
        else:
            return False
        