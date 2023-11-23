class Stack():
    def __init__(self):
        self.List=[None for i in range (1000)]
        self.top=0
        
    def IsEmpty(self):
        if self.top==0:
            return True
        else:
            return False
    
    def Push(self,var):
        self.List[self.top]=var
        self.top+=1
    
    def Pop(self):
        if self.IsEmpty()==False:
            R=self.List[self.top-1]
            self.top-=1
            return R