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
        
        
        
input_var=input()
input_var=input_var.split()

stack=Stack()
for i in range(len(input_var)):
    if (input_var[i]<="Z" and input_var[i]>="A") or (input_var[i]<="z" and input_var[i]>="a"):
        print(input_var[i],end="")
        
    elif input_var[i]=="^":
        while stack.List[stack.top-1]=="^":
            print(stack.Pop(),end="")
        stack.Push(input_var[i])
        
    elif input_var[i]=="*" or input_var[i]=="/":
        while stack.List[stack.top-1]=="/" or stack.List[stack.top-1]=="*" or stack.List[stack.top-1]=="^":
            print(stack.Pop(),end="")
        stack.Push(input_var[i])
        
    elif input_var[i]=="+" or input_var[i]=="-":
        while stack.IsEmpty()==False:
            print(stack.Pop(),end="")
        stack.Push(input_var[i])
            
    elif input_var[i]=="(":
        stack.Push(input_var[i])
        
    elif input_var[i]==")":
        while stack.List[stack.top-1]!="(":
            print(stack.Pop(),end="")
        stack.Pop()
        
while stack.IsEmpty()==False:
    print(stack.Pop(),end="")