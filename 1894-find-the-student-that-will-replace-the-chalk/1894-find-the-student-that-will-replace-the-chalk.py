class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        sum_chalk = 0
        for i in range(n):
            sum_chalk+=chalk[i]
            if sum_chalk>k:
                return i
        k %=sum_chalk
        sum_chalk = 0
        for i in range(n):
            sum_chalk+=chalk[i]
            if sum_chalk>k:
                return i
            