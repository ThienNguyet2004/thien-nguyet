x=int(input())
y=int(input())
while (x>12):
    print('1 nam chi co 12 thang')
    x=int(input('nhap lai thang:'))
if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
    print('thang',x,'nam',y,'co 31 ngay')
if x==4 or x==6 or x==9 or x==11:
    print('thang',x,'nam',y,'co 30 ngay')
if y%4==0 or y%100==0 and y%400!=0 and x==2:
    print('thang 2 nam',y,'co 29 ngay')
else:
    print('thang 2 nam',y,'co 28 ngay')