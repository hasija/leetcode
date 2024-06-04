class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        values = sorted(list(cnt.values()), key=lambda x: -x)
        is_odd = False
        out = 0
        for i in values:
            if i%2==0:
                out+=i
            else:
                is_odd = True
                out+=i-1
        if is_odd:
            return out+1
        return out
            