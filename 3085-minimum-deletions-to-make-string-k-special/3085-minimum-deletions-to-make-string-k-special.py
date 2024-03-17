class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        arr = list(cnt.values())
        arr.sort()
        deleted = 0
        ans = len(word)
        # print ('arr formed',arr)
        for i in range(len(arr)):
            curr_max = 0
            curr = arr[i]
            local_sum = deleted
            for j in range(i+1, len(arr)):
                curr_high = arr[j]
                diff = curr_high-curr-k
                if diff >0:
                    local_sum+=diff
            deleted += curr
            # print ("local sum", local_sum, 'delted', deleted)
            ans = min(ans, local_sum)
        return ans
      