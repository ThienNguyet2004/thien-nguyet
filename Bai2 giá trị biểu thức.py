#nhập input
def nhap_du_lieu():
    x=float(input())
    y=float(input())
    z=float(input())
    return x,y,z

from math import pow    #khai báo thư viện: pow(lũy thừa)
                        #ví dụ: pow(2,3) nghĩa là 2 mũ 3

#tạo hàm f(x,y)=x**2+x*y+y**2-2*x-y
def tinh_fxy(x,y):
    f1=pow(x,2)+x*y+pow(y,2)-2*x-y
    print(f'{f1:.2f}')
    
#tạo hàm f(x,y,z)=x*y*z+x/pow(y,z)
def tinh_fxyz(x,y,z):
    if y!=0:
        f2=x*y*z+x/pow(y,z)
        print(f'{f2:.2f}')
    else :
        print(f'N/A')
        
#gọi hàm nhập input
x,y,z=nhap_du_lieu()

#gọi hàm tính f(x,y)
tinh_fxy(x,y)

#gọi hàm tính f(x,y,z)
tinh_fxyz(x,y,z)