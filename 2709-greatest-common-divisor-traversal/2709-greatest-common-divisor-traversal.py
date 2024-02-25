class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        prime_map = defaultdict(set)
        index_map = defaultdict(set)
        
        # Fill the prime map
        max_n = max(nums)
        prime_nums = []
        if len(nums)==1:
            return True
        nums_set = set(nums)
        nums = list(nums_set)
        
        if 1 in nums_set:
            return False
        for val in range(2, max_n+1):
            flag = False
            for to_check in range(2, int(sqrt(val))+1):
                if val%to_check == 0:
                    flag = True
                    break
            if flag == False:
                prime_nums.append(val)
        
        # fill mapping
        for ind, val in enumerate(nums):
            prime_ind_right = bisect.bisect_right(prime_nums, val)
            for prime in prime_nums[:prime_ind_right]:
                if val%prime==0:
                    prime_map[prime].add(ind)
                    index_map[ind].add(prime)
        
        # print (index_map, prime_map)
        
        def dfs(index, visited_index, visited_prime):
            
            if visited_index[index]:
                return
            visited_index[index]=True
            for prime in index_map[index]:
                if visited_prime[prime]:
                    continue
                visited_prime[prime]=True
                for index_to_visit in prime_map[prime]:
                    dfs(index_to_visit, visited_index,visited_prime)
        
        visited_index = [False]*len(nums)
        visited_prime = defaultdict(bool)
        dfs(0, visited_index, visited_prime)
        
        return sum(visited_index) == len(nums)
        
        
            
                
                    