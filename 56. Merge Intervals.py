class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def merge_array(arr1, arr2):
            start = min(arr1[0],arr2[0])
            end = max(arr1[1],arr2[1])
            return [start,end]
        
        intervals = sorted(intervals)
        old_start=old_end=None
        final_list = []
        
        for x in range(len(intervals)):
            if old_start == old_end == None:
                old_start = intervals[x][0]
                old_end = intervals[x][1]
                final_list.append(intervals[x])
                continue
            curr_start = intervals[x][0]
            curr_end = intervals[x][1]
            if curr_start>=old_start and curr_start<=old_end:
                curr_start,curr_end = merge_array([old_start,old_end],intervals[x])
                final_list.pop(-1)
            old_start = curr_start
            old_end = curr_end
            final_list.append([curr_start,curr_end])
                
        return final_list