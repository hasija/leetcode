class Solution:
    def maximumLength(self, s: str) -> int:
        ans = 0
        n = len(s)
        cnt = defaultdict(int)
        max_sub_len = -1
        
        def check_sub(sub):
            if sub[0]*len(sub) == sub:
                return True
            return False
        
        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]
                if check_sub(sub):
                    cnt[sub]+=1
                    if cnt[sub]>=3 and j-i>max_sub_len:
                        max_sub_len = j-i
        return max_sub_len