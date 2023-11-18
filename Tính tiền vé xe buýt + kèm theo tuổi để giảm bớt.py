#Chon loai ve phu hop
print('Moi quy khach chon loai ve:\n-Ve loai 1: 80000vnd\n-Ve loai 2: 100000vnd')
loaive =int(input('Nhap so 1 hoac 2 tuong ung voi tung loai ve:'))
while  loaive == 1:
    a = 80000
while  loaive == 2:
    a = 100000
while (loaive !=1 and loaive !=2) :
    print('Khong ton tai loai ve nay.')
    loaive=int(input('Moi nhap lai:'))
print("-"*20)

#Kiem tra thong tin khach hang
print('Thong tin co ban cua khach hang bao gom:')
b = input('-Ho ten : ')
c = int(input('-Tuoi : '))
print("-"*20)

#Gia han
print('Moi quy khach gia han cho loai ve da chon.')
d = int(input('Thoi gian gia han (thang): '))
print("-"*20)

#Kiem tra du lieu dau vao
while c<=0:
    print('Du lieu nhap vao bi am hoac bang 0.')
    c = int(input('Moi nhap lai. Tuoi that khach hang: '))
    
while d<=0:
    print('Du lieu nhap vao bi am hoac bang 0.')
    d = int(input('Moi nhap lai.Thoi gian gia han chinh xac (thang): '))

#Thuc hien phan loai doi tuong de dua ra so tien can chi tra
print('Thong bao ve chuong trinh khuyen mai theo do tuoi bao gom 3 loai doi tuong sau:')
print('1.Do tuoi tu 18 tro xuong: mien giam 10%. \n2.Do tuoi tu tren 18 den duoi 60: khong ap dung khuyen mai. \n3.Do tuoi tu 60 tro len: mien giam toan bo.') 
print('-'*20)

if 18<c<60:
    tongsotien=a*d
    print(f'Khach hang {b} khong thuoc doi tuong uu tien.\nSo tien ban phai tra: {tongsotien}')

elif c<=18:
    sotienmoi=a*d-(a*d)*10/100
    print(f'Khach hang {b} thuoc doi tuong uu tien 1.\nSo tien phai tra cua ban se duoc mien giam 10%: {sotienmoi}')

else:
    print(f'Khanh hang {b} thuoc doi tien uu tien 2.\nBan duoc mien giam toan bo.')
print("-"*20)

#Ket thuc
print('Cam on quy khach da su dung dich vu.')