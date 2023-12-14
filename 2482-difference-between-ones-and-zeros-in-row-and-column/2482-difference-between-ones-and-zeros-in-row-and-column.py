class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zeros = defaultdict(int)
        ones = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    ones['r'+str(i)]+=1
                    ones['c'+str(j)]+=1
                else:
                    zeros['r'+str(i)]+=1
                    zeros['c'+str(j)]+=1
        out = [[0]*cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                out[i][j]=ones['r'+str(i)]+ones['c'+str(j)] - (zeros['r'+str(i)]+zeros['c'+str(j)])
        return out