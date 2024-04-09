class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        fwd = []
        bck = []
        curr = None
        for ind,i in enumerate(tickets):
            if k<ind:
                bck.append(i)
            elif k>ind:
                fwd.append(i)
            else:
                curr = i
        count = 0
        # print (fwd, bck)
        for i in fwd:
            if i>=curr:
                count+=curr
            else:
                count+=i
        for i in bck:
            if i>=curr-1:
                count+=curr-1
            else:
                count+=i
        count+=curr
        return count
        
                