#bài này yêu cầu nhớ cách dùng 3 hàm lower() ,title() và swapcase()
#nhap đầu vào 
s=input()

#B1:dùng hàm lower để viết thường tất cả các chữ trong câu
s1=s.lower()
print(s1)

#B2:dùng hàm title để viết hoa các chữ cái đầu tiên từng chữ trong câu
s2=s1.title()
print(s2)

#B3:dùng hàm swapcase để đảo ngược chữ hoa thành thường và ngc lại
s3=s2.swapcase()

#in kết quả cuối cùng
print(s3)