class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = set()
        seen = set()
        for i,j in walls:
            seen.add((i,j))
            walls_set.add((i,j))
        guards_set = set()
        for i,j in guards:
            guards_set.add((i,j))
        
        walls = walls_set
        ROWS = m
        COLS = n
        def check_watch(i,j):
            # check left
            for u in range(i-1,-1,-1):
                if (u,j) in walls or (u,j) in guards_set:
                    break
                seen.add((u,j))
            for d in range(i+1, ROWS):
                if (d,j) in walls or (d,j) in guards_set:
                    break
                seen.add((d,j))
            for l in range(j-1,-1,-1):
                if (i,l) in walls or (i,l) in guards_set:
                    break
                seen.add((i,l))
            for r in range(j+1, COLS):
                if (i,r) in walls or (i,r) in guards_set:
                    break
                seen.add((i,r))
            
                
        
        
        for i,j in guards:
            seen.add((i,j))
            check_watch(i,j)
        
        
        ans = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in seen:
                    ans+=1
        return ans
        
        