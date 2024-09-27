class MyCalendarTwo:

    def __init__(self):
        self.book1 = []
        self.book2 = []
        
    def book(self, start: int, end: int) -> bool:
        curr_b = (start, end)
        # print ("all book2", self.book2)
        for b in self.book2:
            if self.check_overlap(b, curr_b):
                return False
        for b in self.book1:
            if self.check_overlap(b, curr_b):
                new_b = self.get_overlap(b, curr_b)
                self.book2.append(new_b)
                
        else:
            self.book1.append(curr_b)
            return True
    
    def check_overlap(self, b1, b2):
        if b1[0]<b2[1] and b1[1]>b2[0]:
            return True
        b1, b2 = b2, b1
        if b1[0]<b2[1] and b1[1]>b2[0]:
            return True
        return False
        
    def get_overlap(self, b1, b2):
        return max(b1[0], b2[0]), min(b1[1], b2[1])
    
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)