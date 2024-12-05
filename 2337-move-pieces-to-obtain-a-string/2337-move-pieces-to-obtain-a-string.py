class Solution:
    def canChange(self, start: str, target: str) -> bool:
        tar_queue = deque()
        start_queue = deque()
        last = None
        cnt = 0
        n = len(target)
        for idx in range(n):
            if target[idx] != '_':
                tar_queue.append((target[idx],idx))
            if start[idx] != '_':
                start_queue.append((start[idx],idx))
            
        if len(start_queue)!=len(tar_queue):
            return False
        
        while start_queue:
            s, idx1 = start_queue.pop()
            t, idx2 = tar_queue.pop()
            if (s!=t or 
                (s=='L' and idx1<idx2)
                or
                (s=='R' and idx1>idx2)
            ):
                return False
        return True