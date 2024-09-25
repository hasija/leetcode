class TrieNode:
    def __init__(self):
        self.leafs = defaultdict(TrieNode)
        self.count = 0
        self.node = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        node = Trie()
        
        for w in words:
            start = node.root
            for i in w:
                if i in start.leafs:
                    start = start.leafs[i]
                    start.count+=1
                    start.node = i
                else:
                    start.leafs[i]=TrieNode()
                    start = start.leafs[i]
                    start.count+=1
                    start.node = i
        
        
        ################ TESTING TRIE
        # start = node.root
        # check_arr = [start]
        # while check_arr:
        #     tmp = []
        #     for start in check_arr:
        #         # print (start.node, start.count)
        #         for i in start.leafs:
        #             tmp.append(start.leafs[i])
        #     check_arr = tmp
        # return []
        ################ TESTING TRIE
        out = []
        for w in words:
            cnt = 0
            start = node.root
            for char in w:
                if char in start.leafs:
                    start = start.leafs[char]
                    cnt+=start.count
                else:
                    break
            out.append(cnt)
        return out