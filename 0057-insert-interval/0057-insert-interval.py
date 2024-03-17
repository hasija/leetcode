class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        start_int = None
        end_int = None
        ans = []
        inserted = False
        
        if len(intervals)>0 and s<intervals[0][0]:
            start_int = s
        elif len(intervals) == 0:
            return [[s,e]]
        for ind, intv in enumerate(intervals):
            i,j=intv
            if start_int is None and s>=i and s<=j:
                start_int = i
                if e<=j:
                    inserted=True
                    ans.append([i,j])
                # merge
            elif inserted is False and e>=i and e<=j:
                end_int = j
                if start_int is None:
                    start_int = s
                ans.append([start_int, end_int])
                inserted = True
            elif inserted is False and start_int is not None and e<i:
                ans.append([start_int, e])
                ans.append(intv)
                inserted = True
            elif inserted is False and start_int is None and s<i and e>j:
                start_int = s
            elif inserted is False and start_int is None and s<i and e<j:
                ans.append([s, e])
                ans.append(intv)
                inserted = True
            elif inserted is False and start_int is not None and e<i:
                ans.append([start_int, e])
                ans.append(intv)
                inserted = True
            elif start_int is None or inserted is True:
                ans.append(intv)
        if not inserted:
            if start_int == None and end_int == None:
                ans.append([s,e])
            else:
                ans.append([start_int, e])
        
        return ans