class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = defaultdict(int)
        heap = []
        open_heap = [i for i in range(n)]
        meetings = sorted(meetings, key=lambda x: x[0])
        # print (meetings)
        for i,j in meetings:

            
            while heap and heap[0][0] <= i:
                _, room=heapq.heappop(heap)
                heapq.heappush(open_heap, room)
            # print ("meeting",i,j,'heap', heap, open_heap)
            if len(heap)<n:
                room = heapq.heappop(open_heap)
                heapq.heappush(heap,(j, room))
                cnt[room]+=1
            else:
                time, room = heapq.heappop(heap)
                cnt[room]+=1
                extra_time = max(time-i,0)
                heapq.heappush(heap, (j+extra_time, room))
            # print (cnt)
        max_ = 0
        max_r = None
        for i,j in cnt.items():
            if max_<j:
                max_r = i
                max_ = j
            elif max_==j:
                max_r = min(i,max_r)
        # print (cnt)
        return max_r
    
    
    
    
    
    
    
    
    
    
    