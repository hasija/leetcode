class MyCalendar:

    def __init__(self):
        self.bookings = []
        self.n = 0
        
    def book(self, start: int, end: int) -> bool:
        
        s_idx = bisect.bisect_right(self.bookings, (start, end))
        # print(s_idx, self.n)
        if self.n==0:
            self.n+=1
            self.bookings.append((start,end))
            return True
        curr = (start,end)
        if s_idx == 0 and end<=self.bookings[s_idx][0]:
            # print ("here 1")
            self.n+=1
            self.bookings = [curr]+self.bookings
            return True
        elif self.bookings[s_idx-1][1]<=start and s_idx==self.n :
            # print ("here 2")
            self.n+=1
            self.bookings = self.bookings+[curr]
            return True
        elif s_idx!=0 and s_idx!=self.n and self.bookings[s_idx-1][1]<=start and end<=self.bookings[s_idx][0]:
            self.n+=1
            # print ("here 3")
            self.bookings = self.bookings[:s_idx]+[curr]+self.bookings[s_idx:]
            return True
        
        
       
            
        
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)