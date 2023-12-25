class Selection():
    def __init__(self,List) :
        self.List=List

    def Sorting(self):
        for i in range (len(self.List)):
            min = self.List[i]
            min_i=i
            for j in range(i+1,len(List)):
                if self.List[j]<min:
                    min=self.List[j]
                    min_i=j
            swapper=self.List[i]
            self.List[i]=min
            self.List[min_i]=swapper
        return
#---------------------------
# when you want getting number List input in this code:

# List=input()
# List=List.split()

# for i in range(len(List)):
#     List[i]=int(List[i])

# Selection_List=Selection(List)
# Selection_List.Sorting()
# print(Selection_List.List)

#-------------------------------
#when you dont want take the number list from input:

List=[61,5,37,1,26,11,59,15,48,19]
Selection_List=Selection(List)
Selection_List.Sorting()
print(Selection_List.List)