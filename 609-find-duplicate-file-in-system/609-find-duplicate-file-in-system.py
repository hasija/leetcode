class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup = collections.defaultdict(list)
        
        for folder in paths:
            files = folder.split(' ')
            base = files[0]
            for file_ind in range(1, len(files)):
                file = files[file_ind]
                content_start = file.find('(')
                content = file[content_start+1:-1]
                file = file[:content_start]
                full_path = '/'.join([base, file])
                dup[content].append(full_path)
        out = []
        for k,v in dup.items():
            if len(v)>1:
                out.append(v)
        return out