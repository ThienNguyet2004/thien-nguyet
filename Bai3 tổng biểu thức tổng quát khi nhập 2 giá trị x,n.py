#tạo hàm nhập input
def nhap_du_lieu():
    x=float(input())
    n=int(input())
    return x,n

from math import pow #khai báo thư viện nếu cần sử dụng pow

#tạo hàm tính S(x,n)=x+x**2+x**3+...+x**n
def tinh_tong(x,n):
    s=0
    for i in range(1,n+1):
        s+=pow(x,i)
    print(f'{s:.3f}')
        
#gọi hàm nhập input
x,n=nhap_du_lieu()

#gọi hàm tính S(x,n)
tinh_tong(x,n)