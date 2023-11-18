from math import sqrt,pow
#ham nhap du lieu
def nhap_du_lieu():
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    return a, b, c
#ham tinh delta
def tinh_delta(a,b,c):
    delta=pow(b,2)-4*a*c
    return delta
#ham vo nghiem
def pt_vo_nghiem():
    print(f'pt vo nghiem')
#ham nghiem kep   
def pt_nghiem_kep(a,b):
    print(f'pt co nghiem kep la: x1=x2={-b/(2*a):.3f}')
#ham 2 nghiem   
def pt_2_nghiem(a,b,delta):
    print(f'pt co 2 nghiem lan luot la:\nx1={(-b+sqrt(delta))/(2*a):.3f}\nx2={(-b-sqrt(delta))/(2*a):.3f}')
#goi ham nhap du lieu    
a,b,c=nhap_du_lieu()
#goi ham tinh delta
delta=tinh_delta(a,b,c)
print(tinh_delta(a,b,c))
if a!=0:
    if delta<0:
        pt_vo_nghiem()#goi ham vo nghiem
    elif delta==0:
        pt_nghiem_kep(a,b)#goi ham nghiem kep
    else:
        pt_2_nghiem(a,b,delta)#goi ham 2 nghiem 
elif a==0:
    if b!=0:
        print(f'phuong trinh co 1 nghiem: x = {-c/b:.3f}')
    elif b==0:
        print(f'phuong trinh vo nghiem!')