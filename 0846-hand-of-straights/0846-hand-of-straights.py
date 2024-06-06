class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        cnt = OrderedDict(sorted(cnt.items()))
        g_arr = groupSize
        cnt_ind = 0
        try:
            while cnt:
                prev = None
                keys = list(cnt.keys())
                cnt_ind = 0
                for i in range(groupSize):
                    key = keys[cnt_ind]
                    if prev is None:
                        cnt[key]-=1
                        prev = key
                    elif prev+1==key:
                        cnt[key]-=1
                        prev = key
                    else:
                        # print ("inside else")
                        return False
                    cnt_ind+=1
                    if cnt[key]==0:
                        cnt.pop(key)
        except IndexError as e:
            # print (str(e))
            return False
        return True
                
        
            
        
            