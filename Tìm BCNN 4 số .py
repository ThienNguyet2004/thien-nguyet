def nhap_du_lieu():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    d=int(input('d='))
    while a<0:
        a=int(input('a phai la so nguyen duong.\nMoi nhap lai a='))
    while b<0:
        b=int(input('b phai la so nguyen duong.\nMoi nhap lai b='))
    while c<0:
        c=int(input('c phai la so nguyen duong.\nMoi nhap lai c='))
    while d<0:
        d=int(input('d phai la so nguyen duong.\nMoi nhap lai d='))
    return a,b,c,d
def tim_max(a,b,c,d):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    if max<d:
        max=d
    return max

def BCNN(a,b,c,d,max):
    while True:
        if (max%a==0 and max%b==0 and max%c==0 and max%d==0):
            bcnn=max
            break
        else:
            max+=1
    return bcnn
a,b,c,d=nhap_du_lieu()
max=tim_max(a,b,c,d)
bcnn=BCNN(a,b,c,d,max)
print(f'gia tri lon nhat:{tim_max(a,b,c,d)}')
print(f'boi chung nho nhat:{BCNN(a,b,c,d,max)}')
        