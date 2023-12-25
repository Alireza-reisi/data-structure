
class Bubble ():
    def __init__(self,List):
        self.List=List
        self.Flag=True    # when Its True it means the List is sort , when we swaping an item we change it to False , ( if we dont swap any item Flag is True and our work ended) 
        
    def Sorting(self):
        for x in range (len(self.List)-1,0,-1):
            for i in range(x):
                j=i+1
                if (self.List[i]>self.List[j]):
                    self.Flag=False
                    swaper=self.List[i]
                    self.List[i]=self.List[j]
                    self.List[j]=swaper
            if self.Flag==True:
                break
        return

#---------------------------
# when you want getting number List input in this code:

# List=input()
# List=List.split()

# for i in range(len(List)):
#     List[i]=int(List[i])

# Bubble_List=Bubble(List)
# Bubble_List.Sorting()
# print(Bubble_List.List)

#-------------------------------
#when you dont want take the number list from input:

List=[61,5,37,1,26,11,59,15,48,19]
Bubble_List=Bubble(List)
Bubble_List.Sorting()
print(Bubble_List.List)