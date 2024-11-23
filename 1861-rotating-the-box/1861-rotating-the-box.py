class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS = len(box)
        COLS = len(box[0])
        
        res = [['.']*ROWS for i in range(COLS)]
        
        for i in range(ROWS):
            last_row = COLS-1
            for j in range(COLS-1, -1, -1):
                if box[i][j]=='#':
                    res[last_row][ROWS-1-i] = '#'
                    last_row-=1
                elif box[i][j]=='*':
                    res[j][ROWS-1-i] = '*'
                    last_row = j-1
        return res
                    
                