class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(sandwiches)
        cnt2 = Counter(students)
        
        check = None
        if cnt[0]>cnt2[0]:
            check = 0
        elif cnt[1]>cnt2[1]:
            check = 1
        else:
            return 0
        count = 0
        stu = cnt2[check]
        
        for ind, i in enumerate(sandwiches):
            if i == check:
                if stu>0:
                    stu-=1
                else:
                    return len(sandwiches)-ind
                