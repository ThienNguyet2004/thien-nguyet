#nhap biển số xe
s=input()

#cắt s thành 4 phần nhỏ
#VD: 29-B2234.56

dau=s[0:2]   #đầu = 29 (cắt lấy từ vị trí thứ 0 đến thứ trước vị trí thứ 2 của chuỗi s)
than1=s[3]   #thân 1 = B
than2=s[4:8] #thân 2 = 2234
duoi=s[9:]   #đuôi = 56

#kiểm tra xem biển số xe có đủ 11 kí tự không
if len(s)!=11:
    print('No')

else:
    #sử dụng hàm .isalpha() để kiểm tra phần thân 1 có phải chỉ toàn chữ cái không
    #sử dụng hàm .isdigit() để kiểm tra phần thân 2 và đuôi chỉ toàn chữ số không
    if than1.isalpha() and than2.isdigit() and duoi.isdigit():
        
        if 28<int(dau)<32:   #nếu phần đầu là các số 29,30,31 thì là biển số xe hà nội 
            print('Yes')  #in ra đúng
            
        else:
            print('No')  #nếu phần đầu khác 29,30,31 thì in ra sai
    else:
        print('No')