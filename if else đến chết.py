# a:ngay
# b:thang
# c:nam
a=int(input('nhập ngày hiện tại:'))
b=int(input('nhâp tháng hiện tại:'))
c=int(input('nhập năm hiện tại:'))
# x la ngay truoc
# y la ngay mai
if (b==5 or b==7 or b==8 or b==10):
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{x:>02}/{b:>02}/{c}')
        print(f'{y:>02}/{b:>02}/{c}')
# m la thang moi
    if a==1:
        m=b-1
        print(f'30/{m:>02}/{c}')
        print(f'02/{b:>02}/{c}')
    if a==31:
        m=b+1
        print(f'30/{b:>02}/{c}')
        print(f'01/{m:>02}/{c}')
if (b==4 or b==6 or b==9 or b==11):
    if 1<a<30:
        x=a-1
        y=a+1
        print(f'{x:>02}/{b:>02}/{c}')
        print(f'{y:>02}/{b:>02}/{c}')
    if a==1:
        m=b-1
        print(f'31/{m:>02}/{c}')
        print(f'02/{b:>02}/{c}')
    if a==30:
        m=b+1
        print(f'29/{b:>02}/{c}')
        print(f'01/{m:>02}/{c}')
if (b==1):
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{x:>02}/{b:>02}/{c}')
        print(f'{y:>02}/{b:>02}/{c}')
# n la nam moi
    if a==1:
        n=c-1
        print(f'31/12/{n}')
        print(f'02/01/{c}')
    if a==31:
        print(f'30/01/{c}')
        print(f'01/02/{c}')
if (b==12):
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{x:>02}/{b:>02}/{c}')
        print(f'{y:>02}/{b:>02}/{c}')
    if a==1:
        print(f'30/11/{c}')
        print(f'02/12/{c}')
    if a==31:
        n=c+1
        print(f'30/12/{c}')
        print(f'01/01/{n}')
if b==2:
# neu nam nhuan :
    if (((c%4==0) and (c%100!=0)) or (c%400==0)):
        if 1<a<29:
            x=a-1
            y=a+1
            print(f'{x:>02}/02/{c}')
            print(f'{y:>02}/02/{c}')
        if a==1:
            print(f'31/01/{c}')
            print(f'02/02/{c}')
        if a==29:
            print(f'28/02/{c}')
            print(f'01/03/{c}')
# nam khong nhuan :
    else :
        if 1<a<28:
            x=a-1
            y=a+1
            print(f'{x:>02}/02/{c}')
            print(f'{y:>02}/02/{c}')
        if a==1:
            print(f'31/01/{c}')
            print(f'02/02/{c}')
        if a==28:
            print(f'27/02/{c}')
            print(f'01/03/{c}')
if b==3:
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{x:>02}/03/{c}')
        print(f'{y:>02}/03/{c}')
    if a==1:
        if (((c%4==0) and (c%100!=0)) or (c%400==0)):
            print(f'29/02/{c}')
            print(f'02/03/{c}')
        else:
            print(f'28/02/{c}')
            print(f'02/03/{c}')
    if a==31:
        print(f'30/03/{c}')
        print(f'01/04/{c}')