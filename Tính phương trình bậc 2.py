a=int(input())
b=int(input())
c=int(input())
from math import sqrt,pow
def tinh_delta(a,b,c):
    delta=pow(b,2)-4*a*c
    return delta
delta=tinh_delta(a,b,c)
if a==0:
    if b!=0:
        print(f'Phuong trinh co mot nghiem: x = {-c/b:.3f}')
    elif b==0:
        print(f'Phuong trinh vo nghiem!')
if a!=0:    
    if delta<0 :
        print(f'Phuong trinh vo nghiem!')
    elif delta==0:
        print(f'Phuong trinh co nghiem kep: x1 = x2 = {-b/(2*a):.3f}')
    else:
        print(f'Phuong trinh co 2 nghiem: x1 = {(-b+sqrt(delta))/(2*a):.3f} va x2 = {(-b-sqrt(delta))/(2*a):.3f}')