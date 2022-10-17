class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ascii_set = set()
        ascii_arr = [ascii_set.add(x+97) for x in range(26)]
        cpy = sentence
        for val in sentence:
            if ord(val) in ascii_set:
                ascii_set.remove(ord(val))
        if ascii_set:
            return False
        else:
            return True
        