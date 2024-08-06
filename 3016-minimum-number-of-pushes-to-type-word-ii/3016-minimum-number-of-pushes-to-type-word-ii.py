class Solution:
    def minimumPushes(self, word: str) -> int:
        hmap = defaultdict(int)
        idx = 0
        MOD = 8
        cnt = Counter(word)
        cnt_arr = sorted(list(cnt.items()), key=lambda x: -x[1])
        ans = 0
        for key,count in cnt_arr:
            multiplier = 1
            multiplier += idx//MOD
            ans += multiplier*count
            idx+=1
        return ans