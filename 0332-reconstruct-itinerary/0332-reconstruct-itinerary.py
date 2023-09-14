class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        h_map = defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            h_map[a]+=[b]

            res = []
        def visit(start):
            while h_map[start]:
                visit(h_map[start].pop())
            res.append(start)
            
        visit("JFK")
        return res[::-1]