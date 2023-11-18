#n so dong
n=int(input(f'so dong ma tran:'))
#m so cot
m=int(input(f'so cot ma tran:'))
A=[]
for i in range(0,n):
    row=[]
    for j in range(0,m):
        x=int(input(f'A[{i}][{j}]='))
        row=row+[x]
    A=A+[row]
print(A)
for i in range(0,n):
    for j in range(0,m):
        print(f'{A[i][j]}',end=' ')
    print()

tong=0
for i in range(0,n):
    for j in range(0,m):
        tong+=A[i][j]
    
    print(tong,end=' ')
    tong=0