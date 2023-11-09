class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = None
        prev_count = 0
        total = 0
        for char in s:
            if prev!=char:
                prev = char
                prev_count = 1
                total+=1
            else:
                prev_count+=1
                total+=prev_count
        return total%((10**9) + 7)