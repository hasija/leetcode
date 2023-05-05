class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        v = {'a','e','i','o','u'}
        arr = []
        max_v = 0
        for i in range(len(s)):
            
            if len(arr)==k:
                if arr[0] in v:
                    count-=1
                arr.pop(0)
            
            if s[i] in v:
                count+=1
            arr.append(s[i])
            if count ==k:
                return k 
            else:
                max_v = max(max_v, count)
        return max_v
                
        