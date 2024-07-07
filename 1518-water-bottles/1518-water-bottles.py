class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        ans = 0
        while numBottles>0:
            ans+=numBottles
            orig = numBottles
            numBottles = numBottles//numExchange
            empty+=orig%numExchange
            # print ("bottles after drink", empty)
            numBottles += empty//numExchange
            empty%=numExchange
            # print (empty, ans, numBottles)
        return ans