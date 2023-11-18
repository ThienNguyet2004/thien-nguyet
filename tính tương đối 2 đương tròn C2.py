#du lieu duong tron 1:
x1=int(input())
y1=int(input())
r1=float(input())
#du lieu duong tron 2:
x2=int(input())
y2=int(input())
r2=float(input())

from math import sqrt
d=sqrt((x2-x1)**2+(y2-y1)**2)
if d>r1+r2:
    print('NGOAINHAU')
elif d==r1+r2 or r1+d==r2 or r2+d==r1:
    print('TIEPXUC')
elif d+r1<r2 or d+r2<r1:
    print('TRONGNHAU')
else:
    print('GIAONHAU')