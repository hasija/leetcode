class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        arr = [i for i in s]
        ans = 0
        seen = 0
        for i in range(0, n):
            curr = arr[i]
            if curr == '0':
                ans += i-seen
                seen+=1
        return ans