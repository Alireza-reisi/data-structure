
class Merge():
    def __init__(self,List):
        self.List=List
        
    def Sorting(self,First,Last):
        if First<Last:
            av=(First+Last)//2
            s1=self.Sorting(First,av)
            s2=self.Sorting(av+1,Last)
            return (self.Partition(s1,s2))
        elif (First==Last)and(Last<len(self.List)):
            return [self.List[First]]
        else:
            return []
    
    def Partition(self,s1,s2):
        i=0
        j=0
        k=0
        partition_list=[0 for i in range(0,(len(s1)+len(s2)))]
        while (i<len(s1) and j<len(s2)):
            if s1[i]<s2[j]:
                partition_list[k]=s1[i]
                i+=1
                k+=1
            elif s2[j]<s1[i]:
                partition_list[k]=s2[j]
                j+=1
                k+=1
        while (i<len(s1)):
            partition_list[k]=s1[i]
            i+=1
            k+=1
                        
        while (j<len(s2)):
            partition_list[k]=s2[j]
            j+=1
            k+=1
            
        return partition_list
            
            
            
            
            
#---------------------------
# when you want getting number List input in this code:

# List=input()
# List=List.split()

# for i in range(len(List)):
#     List[i]=int(List[i])

# Merge=Merge(List)
# Merge_List=Merge.Sorting(0,len(List))
# print(Merge_List)


#-------------------------------
#when you dont want take the number list from input:

List=[61,5,37,1,26,11,59,15,48,19]
Merge=Merge(List)
Merge_List=Merge.Sorting(0,len(List))
print(Merge_List)