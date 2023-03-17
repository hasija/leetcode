class Tree:
    def __init__(self, val=None, next=[], end=False):
        self.val = val
        self.next = {}
        self.end=False

class Trie:

    def __init__(self):
        self.head = {}
        
    def insert(self, word: str) -> None:
        start = self.head
        for ind, val in enumerate(word):
            if ind!=0:
                start=start.next
            if val in start:
                pass
            else:
                start[val]=Tree(val=val)
            start = start[val]
        start.end=True

    def search(self, word: str) -> bool:
        start = self.head
        for ind, val in enumerate(word):
            if ind!=0:
                check_dict = check_dict.next
            else:
                check_dict = start
                
            if val in check_dict:
                check_dict = check_dict[val]
            else:
                return False
        if check_dict.end:
            return True
        else:
            return False
        
        
    def startsWith(self, prefix: str) -> bool:
        start = self.head
        for ind, val in enumerate(prefix):
            if ind!=0:
                check_dict = check_dict.next
            else:
                check_dict = start
                
            if val in check_dict:
                check_dict = check_dict[val]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)