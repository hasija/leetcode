class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        last = None
        cnt = 0
        ans = ""
        for i in range(n):
            curr = word[i]
            if last!=curr and last is not None:
                while cnt>=9:
                    ans+=str(9)+last
                    cnt-=9
                if cnt>0:
                    ans+=str(cnt)+last
                cnt = 1
                last = curr
            else:
                cnt+=1
                last = curr
        while cnt>=9:
            ans+=str(9)+last
            cnt-=9
        if cnt>0:
            ans+=str(cnt)+last
        return ans