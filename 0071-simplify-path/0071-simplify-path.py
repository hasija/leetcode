class Solution:
    def simplifyPath(self, path: str) -> str:
        path +="/"
        past = 0
        arr = []
        for ind,val in enumerate(path):
            if val=='/':
                tmp = path[past+1:ind]
                if arr and tmp=='..':
                    arr.pop()
                elif tmp and tmp!='.' and tmp!='..':
                    arr.append(tmp)
                past = ind                
        return '/'+'/'.join(arr)
                    
            
        
        
            
            
            