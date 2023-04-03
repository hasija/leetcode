class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boat = 0
        while(l<=r):
            p1 = people[l]
            p2 = people[r]
            if p1+p2<=limit:
                boat+=1
                l+=1
                r-=1
            else:
                r-=1
                boat+=1
        return boat