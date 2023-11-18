# hàm sorted dùng để chia tách các chữ cái và sắp xếp lại chúng
x=input()
y=input()

# kiểm tra xem x và y có cùng số lượng chữ cái hay không và các chữ cái có giống nhau không
# nếu giống thì x và y là Anagram

if sorted(x)==sorted(y) or x!=y:
    print(sorted(x))  #tách và sắp xếp x
    print(sorted(y))  #tách và sắp xếp y
    print('co')
else :
    print('khong')