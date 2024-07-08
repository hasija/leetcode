class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1,n+1)]
        start = 0
        while len(circle)>=2:
            new_ind = start+k-1
            end = new_ind%len(circle)
            circle.pop(end)
            start=end

        return circle[0]