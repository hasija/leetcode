class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        new_ev = []
        for s,e,v in events:
            new_ev.append((s, True, v))
            new_ev.append((e+1, False, v))
        new_ev.sort()
        max_, ans = 0, 0
        for t, start, val in new_ev:
            if start:
                ans = max(ans, max_+val)
            else:
                max_ = max(max_, val)
        return ans