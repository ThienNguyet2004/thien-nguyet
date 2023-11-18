s=input('hay nhap vao 1 so:')
so_nguoc=s[::-1]

print(f'so viet ngc lai :{so_nguoc}')
if s== so_nguoc:
    print(f'so doi xung')
else:
    print(f'so khong doi xung')