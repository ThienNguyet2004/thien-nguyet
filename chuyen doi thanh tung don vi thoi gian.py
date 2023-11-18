a=int(input('nhap tong so giay can chuyen doi:'))
songay=a//86400
sogio=(a%86400)//3600
sophut=(a%86400%3600)//60
sogiay=a%86400%3600%60
print("chuyen doi thanh :")
print(songay,'ngay',sogio,'gio',sophut,'phut',sogiay,'giay')
