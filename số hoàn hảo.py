#số hoàn hảo là số mà tổng các ước nhỏ hơn nó chính bằng số đó
#ví dụ: 6 có 3 ước nhỏ hơn nó là 1,2,3 và 6=1+2+3 nên 6 là số hoàn hảo

def nhap_du_lieu():
    n=int(input('n='))
    while (n<0):
        print('gia tri nhap vao phai nguyen duong')
        n=(input('moi nhap lai :\nn='))
    return n

def kt_so_hoan_hao(n):
    tong=0 
    for i in range(1,n):
        if (n%i==0):#nếu phép chia dư = 0 thì số i là 1 ước của n
            tong+=i #cộng tổng các ước i của n
            
 
    if (tong==n):
        print(f'so {n} la so hoan hao')
    else :
        print(f'so {n} khong la so hoan hao')
#gọi hàm
n=nhap_du_lieu()
kt_so_hoan_hao(n)
            
  