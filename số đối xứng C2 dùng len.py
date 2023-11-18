s=input('hay nhap vao 1 so:')
so_nguoc=''
for i in range(len(s)-1,-1,-1):
    so_nguoc=so_nguoc+s[i]
print(f'so viet ngc lai :{so_nguoc}')
if s== so_nguoc:
    print(f'so doi xung')
else:
    print(f'so khong doi xung')