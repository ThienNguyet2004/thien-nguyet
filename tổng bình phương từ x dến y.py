def nhap_du_lieu():
    x=int(input())
    y=int(input())
    while x<0 and y<0 and x>=y:
        x=int(input())
        y=int(input())
    return x,y
from math import pow
def tong_binh_phuong(x,y):
    tong=0
    for i in range(x,y+1):
        tong+=pow(i,2)
    return tong
x,y=nhap_du_lieu()
print(f'{tong_binh_phuong(x,y):.0f}')