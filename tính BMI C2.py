cannang=float(input())
chieucao=float(input())
x=cannang/(chieucao**2)
if (x<18.5):
    print('Loai 1: Gay')
elif (18.5<x<22.9):
    print('Loai 2: Binh thuong')
elif (23<x<24.9):
    print('Loai 3: Tien beo phi')
elif (25<x<30):
    print('Loai 4: Beo phi do 1')
else :
    print('Loai 5: Beo phi do 2')