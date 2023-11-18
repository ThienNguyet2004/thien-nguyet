#nhập đầu vào
a = input()
b = input()

#ta mặc định gán cho số lần xuất hiện =0
solan = 0

#hàm len để tính độ dài chuỗi 
for i in range(len(a) - len(b) + 1):#giới hạn lặp ở đấy là độ dài chuỗi a trừ đi độ dài chuỗi b
    
    if b == a[i:i+len(b)]:
        #a[i:i+len(b)] nghĩa là đoạn bị cắt trong a từ vị trí i đến hết vị trí (i +độ dài b)
        #nếu chuỗi b mà bằng đoạn bị cắt ra từ chuỗi a thì thực hiện típ lệnh ở dưới đây:
        
        solan += 1
        #mỗi một lần lặp mà điều kiện đúg thì số lần đc cộng thêm 1 (kí hiệu: +=1)
        #VD: -lần lặp 1:  solan= 0(ban đầu ta tự gán) +1 =1
        #    -lần lặp 2:  solan= 1( tính ở lần lặp 1) +1 =2
        #    -lần lặp 3:  ...........

#in số lần lặp cuối cunga=input()
print(solan)