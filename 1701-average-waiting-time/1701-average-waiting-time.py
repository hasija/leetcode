class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = []
        last_prepare = 0
        for arrive,time in customers:
            extra_wait = 0
            if arrive<last_prepare:
                extra_wait = last_prepare-arrive
            total_time = extra_wait+time
            wait.append(total_time)
            last_prepare = max(arrive, last_prepare)+time
        # print(wait)
        return sum(wait)/len(wait)