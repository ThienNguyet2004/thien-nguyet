from math import sqrt

def ktra_input(x1,x2,x3,x4,x5):
    while x1<0:
        x1=int(input(f'gia tri bi am.\nnhap lai gia tri x1='))
    while x2<0:
        x2=int(input(f'gia tri bi am.\nnhap lai gia tri x2='))
    while x3<0:
        x3=int(input(f'gia tri bi am.\nnhap lai gia tri x3='))
    while x4<0:
        x4=int(input(f'gia tri bi am.\nnhap lai gia tri x4='))
    while x5<0:
        x5=int(input(f'gia tri bi am.\nnhap lai gia tri x5='))
       
def tim_min1(list):
    min1=min(list)
    return min1

def tim_min2(list,min1):
    x=set(list)
    x.remove(min1)
    min2=min(x)
    return min2

def ucln(min1,min2,list):
    for i in range(len(list)):
        a=int(sqrt(list[i]))
        for j in range(2,a+1):
            if a%j==0:
                while min1!=min2:
                    if min1>min2:
                        min1-=min2
                    else :
                        min2-=min1
                ucln=min1
                a=0
                
                break
        else:
            ucln=1
            a=0    
        return ucln

def ktra_ucln(ucln,list):
    if ucln>9:
        if ucln>2:
            for k in range(2,ucln):
                for i in range(len(list)):
                    if ucln%k==0 and int(list[i])%k==0:
                        ucln2=int(ucln/k)
                        print(f'uoc chung lon nhat cua {len(list)} so tren la:{ucln2}')
                        break
                    else :
                        ucln2=ucln
                        print(f'uoc chung lon nhat cua {len(list)} so tren la:{ucln2}')
                break
        else :
            ucln2=ucln
            print(f'uoc chung lon nhat cua {len(list)} so tren la:{ucln2}')
        
x1=int(input('x1='))
x2=int(input('x2='))
x3=int(input('x3='))
x4=int(input('x4='))
x5=int(input('x5='))
ktra_input(x1,x2,x3,x4,x5)
list=[x1,x2,x3,x4,x5]
print(f'danh sach cac gia tri:{list}')
list.sort()
print(f'sap xep thu tu danh sach:{list}')
min1=tim_min1(list)
min2=tim_min2(list,min1)
print(f'gia tri nho nhat:{min1}\ngia tri nho thu hai:{min2}')
ucln=ucln(min1,min2,list)
print(f'uoc chung co ban:{ucln}')
ktra_ucln(ucln,list)