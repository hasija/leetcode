class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        posi = defaultdict(list)
        
        self.found = False
        def dfs(r, c, ind, visited):
            if self.found:
                return True
            if ind >=len(word):
                self.found = True
                return True            
            
            if 0<=r+1<rows and 0<=c<cols and (r+1,c) not in visited and board[r+1][c]==word[ind]:
                dfs(r+1, c, ind+1, visited|set([(r+1, c)]))
            
            if 0<=r-1<rows and 0<=c<cols and (r-1,c) not in visited and board[r-1][c]==word[ind]:
                dfs(r-1, c, ind+1, visited|set([(r-1, c)]))
            
            if 0<=r<rows and 0<=c+1<cols and (r,c+1) not in visited and board[r][c+1]==word[ind]:
                dfs(r, c+1, ind+1, visited|set([(r, c+1)]))
            
            if 0<=r<rows and 0<=c-1<cols and (r,c-1) not in visited and board[r][c-1]==word[ind]:
                dfs(r, c-1, ind+1, visited|set([(r, c-1)]))
            
            
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    dfs(r,c, 1, set([(r,c)]))

        return self.found