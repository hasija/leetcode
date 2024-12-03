class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = spaces[::-1]
        ans = ""
        for idx, i in enumerate(s):
            if spaces and idx == spaces[-1]:
                ans+=" "
                spaces.pop()
            ans+=i
        return ans