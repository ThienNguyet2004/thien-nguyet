#thong tin hinh 1
x1=float(input())
y1=float(input())
w1=float(input())
h1=float(input())

#thong tin hinh 2
x2=float(input())
y2=float(input())
w2=float(input())
h2=float(input())

if (x1+w1<x2 or  x2+w2<x1) and (y1+h1<y2 or y2+h2<y1):
    print('KHONGGIAONHAU')
else :
    print('GIAONHAU')