class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_copy = list(str(num))
        cnt = defaultdict(deque)
        for idx, i in enumerate(nums_copy):
            cnt[int(i)].append(idx)
        
        flag = False
        # print ("Cnt list", nums_copy)
        for curr_idx, i in enumerate(nums_copy):
            # print ("looping ", i, cnt)
            curr = int(i)
            for j in range(10, curr, -1):
                if j in cnt and len(cnt[j])>0:
                    swap_idx = cnt[j].pop()
                    nxt_idx = curr_idx
                    flag = True
                    break
            if flag:
                break
            else:
                cnt[int(i)].popleft()
        if flag:
            # print ('Idx to be changed',swap_idx, curr_idx)
            nums_copy[swap_idx], nums_copy[curr_idx] = nums_copy[curr_idx], nums_copy[swap_idx]
            return int(''.join(nums_copy))
        else:
            return num
            
        