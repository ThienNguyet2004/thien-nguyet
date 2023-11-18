n=int(input())
list=[]
tong1=0
tong2=0
tong3=0
for i in range(n):
    x=float(input())
    while x<0 or x>10:
        x=float(input())
    list.append(x)    
    a=float(list[i])
    if 7<=a<8:
        tong1+=1200000
    elif 8<=a<9:
        tong2+=1400000
    elif 9<=a<=10:
        tong3+=1800000
tong=tong1+tong2+tong3
print(tong)