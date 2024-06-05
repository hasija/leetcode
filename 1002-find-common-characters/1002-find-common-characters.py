class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt_arr = [Counter(w) for w in words]
        all_chars = set()
        for cnt in cnt_arr:
            all_chars.update(cnt.keys())
        out = []
        for char in all_chars:
            count = float('inf')
            for cnt in cnt_arr:
                val = cnt.get(char)
                if val is None:
                    break
                else:
                    count = min(count, val)
            else:
                # print ("out", char, count)
                out+=[char]*count
        return out
        