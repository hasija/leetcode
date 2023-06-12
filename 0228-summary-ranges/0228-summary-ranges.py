class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        prev= None
        last = None
        out = []
        for i in nums:
            # print ("this is i", i, prev, last)
            if prev is None:
                # print ("prev is none")
                prev = i
                last = i
                continue
            if i-last==1:
                # print ("last-i is 1")
                last=i
                continue
            else:
                # print ("value un,equal")
                if last!=prev:
                    out.append(str(prev)+"->"+str(last))
                else:
                    out.append(str(last))
                prev = i
                last = i
        
        if prev is not None:
            # print ("coming here", last, prev)
            if last!=prev:
                out.append((str(prev)+"->"+str(last)))
            else:
                out.append(str(last))
        return out