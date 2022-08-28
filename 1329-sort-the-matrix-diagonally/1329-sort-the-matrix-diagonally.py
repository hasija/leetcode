class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        sort_dict = collections.defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                sort_dict[row-col].append(mat[row][col])
        
        
        for k,v in sort_dict.items():
            v.sort()
            sort_dict[k]=v
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col]=sort_dict[row-col][0]
                sort_dict[row-col].pop(0)
        return mat
        