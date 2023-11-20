class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total=0
        final_idx={}
        for ind, i in enumerate(garbage):
            for char in i:
                if char=='M':
                    # tm+=1
                    final_idx['M']=ind
                elif char=='P':
                    # tp+=1
                    final_idx['P']=ind
                elif char=='G':
                    # tg+=1
                    final_idx['G']=ind
                total+=1
        pfx_sum = []
        old=0
        for i in travel:
            pfx_sum.append(i+old)
            old=pfx_sum[-1]
        
        for char, idx in final_idx.items():
            if idx-1>=0:
                total+=pfx_sum[idx-1]
        return total
        
                
            