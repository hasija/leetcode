class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        for i in s:
            cnt[i]+=1
        for i in 'abc':
            if cnt[i]<k:
                return -1
        
        limit = defaultdict(int)
        for i in 'abc':
            limit[i] = cnt[i]-k
        
        l = 0
        r = 0
        new_cnt = defaultdict(int)
        ans = 0
        for r in range(len(s)):
            curr = s[r]
            new_cnt[curr]+=1
            while new_cnt[curr]>limit[curr]:
                new_cnt[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return len(s)-ans