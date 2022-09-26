class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = collections.defaultdict(set)
        un_equal = []
        
        self.check = False
        def check_meet(a, b, visited):
            # print ("check meet", a, b)
            if self.check==True:
                return True
            if a==b:
                # print ("here1")
                self.check=True
                return True
            visited.add(a)
            for val in equal[a]:
                # print ("here2", val)
                if val in visited:
                    # print ("here3")
                    continue
                # print ("here4")
                check_meet(val ,b, visited)
            return False
    
    

        for eq in equations:
            x1=eq[0]
            x2=eq[3]
            comp = eq[1]
            if x1==x2 and comp=='!':
                return False
            if comp == '=' :
                equal[x1].add(x2)
                equal[x2].add(x1)
            elif comp == '!' :
                un_equal.append((x1,x2))
        
        # print (equal,'equal check')
        
        # print (un_equal,'unequal check')
        # Check unequal
        
        for a,b in un_equal:
            self.check = False
            check_meet(a,b,set())
            if self.check:
                return False
        return True
        
        
                