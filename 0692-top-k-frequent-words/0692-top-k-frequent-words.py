class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w_dict = collections.defaultdict(int)
        for val in words:
            w_dict[val]+=1
        
        arr = [(v,k) for k,v in w_dict.items()]
        
        arr = sorted(arr, key= lambda x: (-x[0],x[1]) )
        new_arr = []
        for ind in range(k):
            new_arr.append(arr[ind][1])
        return new_arr