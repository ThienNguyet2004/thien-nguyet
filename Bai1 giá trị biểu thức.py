#nhập input
def nhap_du_lieu():
    x=float(input())
    return x

from math import sqrt,pow     #khai báo thư viện: sqrt(phép lấy căn bậc 2) và pow(phép lấy lũy thừa)

#fx=-2*(x-3)     khi -1<=x<=1
#fx=sqrt(pow(x,2)-1) khi x>1
def tinh_fx(x):
    if -1<=x<=1:
        print(f'{-2*(x-3):.2f}')        
    elif x>1:
        print(f'{sqrt(pow(x,2)-1):.2f}')
    else :
        print(f'0.00')
        
#gx=pow(x,2)+1    khi x>2
#gx=2*x-1         khi -2<=x<=2
#gx=6-5*x         khi x<-2
def tinh_gx(x):
    if x>2:
        print(f'{pow(x,2)+1:.2f}')
    elif -2<=x<=2:
        print(f'{2*x-1:.2f}')
    else :
        print(f'{6-5*x:.2f}')
     
#nhap gia tri va in ket qua
x=nhap_du_lieu()
tinh_fx(x)
tinh_gx(x)

        
    
    