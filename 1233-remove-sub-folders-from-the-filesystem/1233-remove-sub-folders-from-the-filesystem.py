class Trie:
    def __init__(self, val=None):
        self.node = {}
        self.terminate = False
        self.val = val
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        top_path = Trie(val='')
        
        def dfs(tree, path):
            curr = path[0]
            if len(path)==1:
                
                if curr in tree.node:
                    tree.node[curr].terminate=True
                else:
                    tree.node[curr] = Trie(val=curr)
                    tree.node[curr].terminate=True
                    
            else:
                
                if curr not in tree.node:
                    tree.node[curr] = Trie(val=curr)
                    tree = tree.node[curr]
                else:
                    tree = tree.node[curr]
                if tree.terminate is False:
                    dfs(tree, path[1:])
        
        for path in folder:
            all_paths = path.split('/')
            all_paths = [p for p in all_paths if p]
            dfs(top_path, all_paths)
        out = []
        # print ("this is top path", top_path.node)
        self.ans = []
        def dfs2(tree, past_str):
            # print ("looping dfs2", past_str)
            if tree.terminate:
                self.ans.append(past_str+'/'+tree.val)
                return
            ans = []
            for node, nxt_tree in tree.node.items():
                curr_dfs_out = dfs2(nxt_tree, past_str+'/'+tree.val)
                
        for node, nxt_tree in top_path.node.items():
            dfs2(nxt_tree,'')
        return self.ans