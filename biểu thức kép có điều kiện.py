x=float(input())
from math import sqrt , e
#tinh f1
if x>0:
    f1=3*x+sqrt(x)
    print(f'{f1:.3f}')
elif x<=0:
    f2=(e**x)+4
    print(f'{f2:.3f}')
#tinh f2
if x>=1:
    f3=sqrt(x**2+1)
    print(f'{f3:.3f}')
elif -1<x<1:
    f4=3*x+5
    print(f'{f4:.3f}')
elif x<=-1:
    f5=x**2+2*x-1
    print(f'{f5:.3f}')