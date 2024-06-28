class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_imp = defaultdict(int)
        for i,j in roads:
            city_imp[i]+=1
            city_imp[j]+=1
        arr = [(k,v)for k,v in city_imp.items()]
        new_arr = sorted(arr, key = lambda x: -x[1] )
        city_number = [0]*n
        for city,val in new_arr:
            city_number[city] = n
            n-=1
        ans = 0
        for i,j in roads:
            ans+=city_number[i]+city_number[j]
        return ans