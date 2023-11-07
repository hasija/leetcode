class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        total = len(dist)
        time = [dist[i]/speed[i] for i in range(total)]
        time = sorted(time)
        for i in range(1,total):
            t = time[i]-i
            if t <=0:
                return i
        return total