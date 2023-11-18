def nhap_du_lieu():
    n=int(input())
    if n<=1 or n>=10000:
            print('N/A')
            
    return n
def tinh_tong(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print(s)
n=nhap_du_lieu()
if 1<n<10000:
    tinh_tong(n)
