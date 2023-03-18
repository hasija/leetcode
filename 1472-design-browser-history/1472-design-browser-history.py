class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.max = 1

    def visit(self, url: str) -> None:
        
        self.curr+=1
        if self.curr>=self.max:
            self.history.append(url)
            self.max+=1
        else:
            self.history[self.curr]=url
            i = self.curr+1
            new_max=0
            while (i<self.max):
                self.history.pop()
                i+=1
                new_max+=1
            self.max-=new_max

    def back(self, steps: int) -> str:
        # print (self.history)
        if self.curr==self.max-1 and self.curr==0:
            # print ("move is false", steps)
            move=False
        else:
            move=True
        self.curr-=steps
        if self.curr<0:
            self.curr=0
        # print("back", self.history, self.curr, self.max)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:

            
        self.curr+=steps
        if self.curr>=self.max:
            self.curr=self.max-1

        
        # print("fwd", self.history, self.curr, self.max)

        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)