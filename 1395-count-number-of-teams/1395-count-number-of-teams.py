class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        self.ans = 0
        dp = [[0,0] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if rating[j]<rating[i]:
                    dp[i][0]+=1
                    dp[i][1]+=dp[j][0]
        self.ans += sum([i for _,i in dp])
        dp = [[0,0] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if rating[j]>rating[i]:
                    dp[i][0]+=1
                    dp[i][1]+=dp[j][0]
        self.ans += sum([i for _,i in dp])
        return self.ans
            