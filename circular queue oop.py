class queue:
    def __init__(self,size):
        self.List=[None for i in range(size)]
        self.front=0
        self.rear=0
        self.size=size
        
    def IsEmpty(self):
        if self.front==self.rear:
            return True
        
    def IsFull(self):
        if ((self.rear+1)%self.size)==self.front:
            return True
        
    def Enqueue(self,input_var):  # add to queue
        if self.IsFull()==True:
            print("The queue is full!")
            return
        else:
            self.List[self.rear]=input_var
            self.rear=(self.rear+1)%self.size
    
    def Dequeue(self): # remove from queue
        if self.IsEmpty()==True:
            print("The queue is empty!")
            return
        else:
            return_value=self.List[self.front]
            self.List[self.front]=None
            self.front=(self.front+1) % self.size
            return return_value
    
    def Peek(self): # show front value without removing
        if self.IsEmpty()==True:
            print("The queue is empty!")
            return None
        else:
            return self.List[self.front]

    def ReverseQueue(self):
        if self.IsEmpty==True:
            print("The queue is empty!")
            return 
        else:
            i=self.front
            j=(self.rear-1)%self.size
            while i<j:
                self.List[i],self.List[j]=self.List[j],self.List[i]
                i+=1
                j=1
            return
    
    
# =======================================================    



# a=queue(5)
# x=a.Dequeue()
# print(x)
# a.Enqueue(1)
# print(a.List)
# a.Enqueue(2)
# print(a.List)
# a.Enqueue(3)
# print(a.List)
# a.Enqueue(4)
# print(a.List)
# a.Enqueue(5)
# print(a.List)
# a.ReverseQueue()

# print(a.List)

# khaste nabashid
