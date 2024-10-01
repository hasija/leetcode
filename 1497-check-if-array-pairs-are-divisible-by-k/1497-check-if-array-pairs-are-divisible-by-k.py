class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        for i in arr:
            # print ('start',i, hmap)
            curr_mod = i%k
            left = k-curr_mod if curr_mod else 0
            # print ("check for left", left)
            if left in hmap:
                hmap[left]-=1
                if hmap[left]==0:
                    hmap.pop(left)
            else:
                hmap[curr_mod]+=1
        # print (hmap)
        return False if hmap else True