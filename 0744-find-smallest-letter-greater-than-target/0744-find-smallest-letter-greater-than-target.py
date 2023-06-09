class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_val = float('inf')
        target = ord(target)
        for val in letters:
            # print (type(min_val), type(target))
            if min_val>ord(val)>target:
                min_val = ord(val)
        # print (chr(min_val))
        try:
            return chr(min_val)
        except:
            return letters[0]