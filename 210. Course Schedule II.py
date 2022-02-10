class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def check_if_free(course):
            for pending_course in pre_req[course]:
                if int(pending_course) not in courses_done:
                    return False
                else:
                    pass
            return True
        pre_req = {}
        courses_done = set()
        for course, pre in prerequisites:
            if course in pre_req:
                pre_req[course].add(str(pre))
            else:
                pre_req[course]=set([str(pre)])
        # print(pre_req)
        curr_ind = 0
        final_arr = []
        course_arr = [x for x in range(numCourses)]
        counter = len(course_arr)
        
        while course_arr !=[]:
            curr_course = course_arr[curr_ind]
            # print (f"current course: {curr_course}")
            if curr_course not in pre_req:
                # print ("course in free", curr_course)
                final_arr.append(curr_course)
                courses_done.add(curr_course)
                del course_arr[curr_ind]
            elif curr_course in pre_req:
                # print ("course in pre req", curr_course)
                if check_if_free(curr_course):
                    # print ("coursse in pre req is free", curr_course)
                    final_arr.append(curr_course)
                    courses_done.add(curr_course)
                    del course_arr[curr_ind]
                else:
                    # print ("noting found")
                    curr_ind+=1
            if curr_ind>=len(course_arr):
                curr_ind=0
                if counter==len(course_arr):
                    return []
                else:
                    counter = len(course_arr)
        return final_arr