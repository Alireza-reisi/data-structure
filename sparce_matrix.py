def Sparce(List,n):
    z=0
    Matrix=[["i","j",None]]
    for i in range (n):
        for j in range (n):
            if List[i][j]!=0:
                Matrix_i=[i,j,List[i][j]]
                Matrix.append(Matrix_i)
                z=z+1
    Matrix[0][2]=z
    return Matrix

a=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,0,0,0,0,0],
    [0,0,2,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,8,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,1,0,0,0]
]
z=Sparce(a,10)
for i in range (len(z)):
    print(z[i])