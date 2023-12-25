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
        
                
# ===============================

input_var=input()
input_var=input_var.split()
input_var=input_var[::-1]
output_var=[None for i in range (len(input_var))]

# =================================

stack=Stack()
j=0
for i in range(len(input_var)):
    if (input_var[i]<="Z" and input_var[i]>="A") or (input_var[i]<="z" and input_var[i]>="a"):
        output_var[j]=input_var[i]
        j+=1
        
    elif input_var[i]=="^":
        while stack.List[stack.top-1]=="^":
            output_var[j]=stack.Pop()
            j+=1
        stack.Push(input_var[i])
        
    elif input_var[i]=="*" or input_var[i]=="/":
        while stack.List[stack.top-1]=="/" or stack.List[stack.top-1]=="*" or stack.List[stack.top-1]=="^":
            output_var[j]=stack.Pop()
            j+=1
        stack.Push(input_var[i])
        
    elif input_var[i]=="+" or input_var[i]=="-":
        while stack.IsEmpty()==False:
            output_var[j]=stack.Pop()
            j+=1
        stack.Push(input_var[i])
            
    elif input_var[i]=="(":
        stack.Push(input_var[i])
        
    elif input_var[i]=="(":
        while stack.List[stack.top-1]!=")":
            output_var[j]=stack.Pop()
            j+=1
        stack.Pop()
        
while stack.IsEmpty()==False:
    output_var[j]=stack.Pop()
    j+=1
    
# ==========================================

output_var=output_var[::-1]
for x in output_var:
    print(x,end="")