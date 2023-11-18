import math
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n <= 0
while n < 0:
       print("Vui long nhap so tu nhien!")
       n = int(input())
elif n < 2:
       print("{} khong la so nguyen to!".format(n))
else:
       #Su dung vong lap for de duyet cac so tu 2 den can bac hai cua n
    for i in range(2, int(math.sqrt(n))+1):
           #Kiem tra tinh chia het
           if n % i == 0:
               print("{} khong la so nguyen to!".format(n))
               #Thoat vong lap
               break
       #Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
    else:
           print("{} la so nguyen to!".format(n))
