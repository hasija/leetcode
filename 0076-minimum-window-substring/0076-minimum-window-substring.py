class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r=-1
        l=0
        new_str = ""
        count_dict = collections.Counter(t)
        curr_dict = collections.defaultdict(int)
        
        def check_valid(new_str):
            for k,v in count_dict.items():
                if k in curr_dict and v<=curr_dict[k]:
                    pass
                else:
                    return False
            return True
        max_len = float('inf')
        min_out = ""
        while (r<len(s)):
            if check_valid(new_str):
                new_len = len(new_str)
                if max_len>new_len:
                    max_len = new_len
                    min_out = new_str
                l+=1
                curr_dict[new_str[0]]-=1
                new_str = new_str[1:]
            else:
                if r+1==len(s):
                    break
                r+=1
                new_str+=s[r]
                curr_dict[s[r]]+=1
        return min_out
        