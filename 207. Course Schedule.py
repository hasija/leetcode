import copy

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        valid_list = [0]*numCourses
        def check_cycle(k):
            # print("1", valid_list)
            if valid_list[k]==-1:
                # print("2")
                return True
            elif valid_list[k] == 1:
                # print("3")
                return False
            if k not in graph or not graph[k]:
                # print("4")
                valid_list[k] = 1
                return False
            else:
                # print("5")
                valid_list[k] = -1
            # print("6")
            for item in graph[k]:
                # print (f"loop: {item}")
                if check_cycle(item):
                    return True
                else:
                    valid_list[item]=1
            
        graph = {}
        if prerequisites:
            for req in range(len(prerequisites)):
                if prerequisites[req][0] >=numCourses:
                    continue
                if prerequisites[req][0] in graph:
                    graph[prerequisites[req][0]].append(prerequisites[req][1])
                else:
                    graph[prerequisites[req][0]] = [prerequisites[req][1]]
                if prerequisites[req][0] <numCourses and prerequisites[req][1]>=numCourses:
                    return False
        #check for cycle
        # print(graph)
        for k in graph:
            # print(f"start: {k}")
            if check_cycle(k):
                return False
            else:
                valid_list[k]=1
        return True

                
                