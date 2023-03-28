class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        day_set = set(days)
        def find_cost(day):
            # print ("currnt day", day)
            if day>days[-1]:
                return 0
            if day not in day_set:
                return find_cost(day+1)
            # day = days[ind]
            if day in dp:
                return dp[day]

            dp[day]=min(find_cost(day+1)+costs[0], find_cost(day+7)+costs[1], find_cost(day+30)+costs[2])
            # print ("iutput day and val", day, dp[day])
            return dp[day]
        find_cost(1)
        return dp[days[0]]