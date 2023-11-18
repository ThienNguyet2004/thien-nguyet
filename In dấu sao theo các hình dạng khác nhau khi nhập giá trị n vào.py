#in ra cac dang hinh hoc = dau *
x=int(input('nhap so nguyen de dinh dang:'))
print('-'*30)
i=0
#hinh 1
print('-hinh tam giac can ngang:')
print('')
for i in range(1,x+1):
    for n in range(1,x*2,2):
        a='*'*n
        print(f'{a:^{x*2+1}}')
    break
print('-'*30)
#hinh 2
print('-hinh chu nhat:')
print('')
for i in range(1,x+1):
    print('*'*x)
print('-'*30)
#hinh 3
print('-hinh tam giac can doc:')
print('')
for i in range(1,x+1):
    for n in range(1,x*2,2):
        a='*'*n
        print(f'{a:<{x*2}}')

    for n in range(x*2-3,0,-2):
        b='*'*n
        print(f'{b:<{x*2}}')
    break
print('-'*30)