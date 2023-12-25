class Insertion():
    def __init__(self,List):
        self.List=List
        
        
    def Sorting(self):
        for i in range(1,len(self.List)):
            for j in range(i,-1,-1):
                if (self.List[j]<self.List[j-1])and j>0:
                    swapper=self.List[j]
                    self.List[j]=self.List[j-1]
                    self.List[j-1]=swapper
                else:
                    break
                
            
            
            #---------------------------
# when you want getting number List input in this code:

# List=input()
# List=List.split()

# for i in range(len(List)):
#     List[i]=int(List[i])

# Insertion_List=Insertion(List)
# Insertion_List.Sorting()
# print(Insertion_List.List)

#-------------------------------
#when you dont want take the number list from input:

List=[61,5,37,1,26,11,59,15,48,19]
Insertion_List=Insertion(List)
Insertion_List.Sorting()
print(Insertion_List.List)    
            
        