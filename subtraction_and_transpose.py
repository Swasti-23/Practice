R=int(input("enter the number of rows:"))
C=int(input("Enter the number of columns:"))
matrix_1=[]
matrix_2=[]
print("Enter the entries rowwise!")
for i in range(R):          
    a =[int(i) for i in input().split(" ")]
    matrix_1.append(a)

for i in range(R):          
    a =[int(i) for i in input().split(" ")]
    matrix_2.append(a)
print(matrix_1)
print(matrix_2)

#substarction
matrix_3=[]
for i in range(R):
  r=[]
  for j in range(C):
    r.append(matrix_1[i][j]-matrix_2[i][j])
  matrix_3.append(r)
print(matrix_3)

#transpose
trans=[]
for i in range(C):
    r=[]
    for j in range(R):
        r.append(matrix_3[j][i])
    trans.append(r)
print(trans)
    