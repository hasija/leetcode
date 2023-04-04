class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        last = set()
        n = len(s)
        for i in range(n):
            val = s[i]
            # print (i, val)
            if val in last:
                count+=1
                last={val}
            else:
                last.add(val)
            # print (count)
        if last:
            count+=1
        return count