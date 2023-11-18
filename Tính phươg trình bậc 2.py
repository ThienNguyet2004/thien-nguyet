a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

while a==0:
    print('gia tri a phai khac 0.')
    a=float(input('moi nhap lai: a='))

from math import sqrt,pow

delta=pow(b,2)-4*a*c

if delta<0:
    print(f'pt vo nghiem')
elif delta==0:
    
    print(f'pt co nghiem kep la x1=x2={-b/(2*a):.3f}')
elif delta>0:
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    print(f'pt co 2 nghiem la:\nx1={x1:.3f}\nx2={x2:.3f}')
