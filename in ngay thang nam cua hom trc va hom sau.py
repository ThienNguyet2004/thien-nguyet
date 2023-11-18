# a :ngay
a=int(input())
# b :thang
b=int(input())
# c :nam
c=int(input())

if (b==5 or b==7 or b==8 or b==10):
# x ngay hom truoc
# y ngay hom sau
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{format(x,">02")}/{format(b,">02")}/{c}')
        print(f'{format(y,">02")}/{format(b,">02")}/{c}')
    if a==1:
# m thang moi
        m=b-1
        print(f'30/{format(m,">02")}/{c}')
        print(f'02/{format(b,">02")}/{c}')
    if a==31:
        m=b+1
        print(f'30/{format(b,">02")}/{c}')
        print(f'01/{format(m,">02")}/{c}')
        
if (b==4 or b==6 or b==9 or b==11):
    if 1<a<30:
        x=a-1
        y=a+1
        print(f'{format(x,">02")}/{format(b,">02")}/{c}')
        print(f'{format(y,">02")}/{format(b,">02")}/{c}')
    if a==1:
        m=b-1
        print(f'31/{format(m,">02")}/{c}')
        print(f'02/{format(b,">02")}/{c}')
    if a==30:
        m=b+1
        print(f'29/{format(b,">02")}/{c}')
        print(f'01/{format(m,">02")}/{c}')
        
if (b==1):
# n nam moi
    if 1<a<31:
        x=a-1
        y=a+1
        print(f'{format(x,">02")}/{format(b,">02")}/{c}')
        print(f'{format(y,">02")}/{format(b,">02")}/{c}')
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
        print(f'{format(x,">02")}/{format(b,">02")}/{c}')
        print(f'{format(y,">02")}/{format(b,">02")}/{c}')
    if a==1:
        print(f'30/11/{c}')
        print(f'02/12/{c}')
    if a==31:
        n=c+1
        print(f'30/12/{c}')
        print(f'01/01/{n}')
        
if b==2:
    if (((c%4==0) and (c%100!=0)) or (c%400==0)):
        if 1<a<29:
            x=a-1
            y=a+1
            print(f'{format(x,">02")}/02/{c}')
            print(f'{format(y,">02")}/02/{c}')
        if a==1:
            print(f'31/01/{c}')
            print(f'02/02/{c}')
        if a==29:
            print(f'28/02/{c}')
            print(f'01/03/{c}')
    else :
        if 1<a<28:
            x=a-1
            y=a+1
            print(f'{format(x,">02")}/02/{c}')
            print(f'{format(y,">02")}/02/{c}')
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
        print(f'{format(x,">02")}/03/{c}')
        print(f'{format(y,">02")}/03/{c}')
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
