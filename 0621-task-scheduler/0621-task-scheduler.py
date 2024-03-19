class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = []
        coolcount = defaultdict(int)
        cnt = Counter(tasks)
        tasks_q = [-j for i,j in cnt.items()]
        heapq.heapify(tasks_q)
        ans = 0

        while True:
            cycle = 0
            used = []
            curr_cnt = 0
            while tasks_q and cycle<n+1:
                cycle+=1
                task = heapq.heappop(tasks_q)
                task *=-1
                used.append(task-1) if task-1>0 else None
            
            
            if not tasks_q and not used:
                ans+=cycle
                return ans
            else:
                ans+=n+1
                for task in used:
                    heapq.heappush(tasks_q, -task)
                
            
                
            
            
            
                
            
        
        