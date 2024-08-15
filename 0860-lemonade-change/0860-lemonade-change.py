class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = {5:0,10:0,20:0}
        for i in bills:
            if i==5:
                cnt[i]+=1
            elif i==10 and cnt[5]>0:
                cnt[5]-=1
                cnt[10]+=1
            elif i==20 and (cnt[10]>0 and cnt[5]>0):
                cnt[20]+=1
                cnt[10]-=1
                cnt[5]-=1
            elif i==20 and cnt[5]>2:
                cnt[5]-=3
                cnt[20]+=1
            else:
                return False
        return True
                