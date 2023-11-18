from math import pow
def nhap_du_lieu():
    n=int(input())
    while n<0:
        n=int(input())
    return n
def so_chu_so(n):
    x=0
    while n!=0:
        x+=1
        n=n//10
    return x
def tong_luy_thua(n,x):
    luythua=0
    while n!=0:
        s=n%10
        luythua+=pow(s,x)
        n=n//10
    return luythua
n=nhap_du_lieu()
x=so_chu_so(n)
luythua=tong_luy_thua(n,x)
if luythua==n:
    print('Co')
else:
    print('Khong')