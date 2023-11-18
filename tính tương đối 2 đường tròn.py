x1=float(input())
y1=float(input())
r1=float(input())
x2=float(input())
y2=float(input())
r2=float(input())
import math
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
c=r1+r2
if d>c:
    print('NGOAINHAU')
elif d<c:
    if d==0 or r1+d<r2 or r2+d<r1:
        print('TRONGNHAU')
    
    elif (r1-r2==d) or (r2-r1==d):
        print('TIEPXUC')
    else :
        print('GIAONHAU')
elif (c==d) :
    print('TIEPXUC')
