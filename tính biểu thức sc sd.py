n=int(input())
while n<0:
    n=int(input())
from math import sqrt
def tinh_sc(n):
    s=0
    for i in range(1,n+1):
        s+=3
        s=sqrt(s)
    return s
    
def tinh_sd(n):
    s=1
    tong=0
    for i in range(1,n+1):
        s*=i
        tong+=s
    return tong
    
print(f'sc={tinh_sc(n):.3f}')
print(f'sd={tinh_sd(n):.3f}')