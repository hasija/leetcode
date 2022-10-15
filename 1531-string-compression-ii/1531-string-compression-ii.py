class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def get_length(start, last_count, s_str, left):
            # print (start, 'started')
            if left<0:
                return float('inf')
            if start>=len(s):
                # print ("case over")
                return 0
            # if we are facing same integer as prev then we sum it up
            if s[start]==s_str:
                # print ("same found", last_count)
                add_count = 0
                if last_count==1 or last_count ==9 or last_count==99:
                    add_count = 1
                # print ("was a similar one so adding one", add_count, last_count, start)
                return add_count+get_length(start+1, last_count+1, s_str, left)
            # If not same as prev string
            else:
                #either delete the string or count the string
                # count the string
                count_str = 1+get_length(start+1, 1, s[start], left)
                delete_count = get_length(start+1, last_count, s_str, left-1)
                min_count = min(count_str, delete_count)
                # print (count_str, delete_count,'min of two')
                return min_count
        return get_length(0, 0, "", k)
        
            
            
        