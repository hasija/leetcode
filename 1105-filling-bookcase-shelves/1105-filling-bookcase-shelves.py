class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        memo = {}
        def dp(i, cnt_w, cnt_h):
            if (i, cnt_w, cnt_h) in memo:
                return memo[(i,cnt_w, cnt_h)]
            ans = 0
            if i>=n:
                return cnt_h
            w,h = books[i]
            if cnt_w+w<=shelfWidth:
                memo[(i,cnt_w, cnt_h)] = min(dp(i+1, cnt_w+w, max(cnt_h,h)),
                    dp(i+1, w, h)+cnt_h)
            else:
                memo[(i,cnt_w, cnt_h)] = dp(i+1, w, h)+cnt_h
            return memo[(i,cnt_w, cnt_h)]
        return dp(0, 0, 0)