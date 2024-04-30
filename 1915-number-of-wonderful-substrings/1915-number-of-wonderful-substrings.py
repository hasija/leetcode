class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        mask = 0
        seen = {0:1}
        for ind, i in enumerate(word):
            bit = 1<<(ord(i)-97)
            mask ^=bit
            if mask in seen:
                ans+=seen[mask]
                seen[mask]+=1
            else:
                seen[mask]=1
            # print ("seen", seen)
            for j in range(10):
                # if ind == 2:
                    # print ("looking for ", mask^(1<<j))
                if mask^(1<<j) in seen:
                    # print ("found")
                    ans+=seen[mask^(1<<j)]
            # print (ans)
        return ans
            