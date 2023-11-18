# từ khóa yield có vai trò tương tự như return đó là trả về giá trị cho biến
# tuy nhiên return chỉ trả về duy nhất 1 giá trị
# còn yield sẽ trả về 1 loạt giá trị cùng 1 lúc cho chỉ 1 biến (mà không phải đặt tên biến mới cho mỗi lần muốn lưu 1 giá trị)
# thuận tiện cho việc lưu thành danh sách
x=int(input())
y=int(input())
def so(x,y):
    so1=x+y
    so2=(x+y)*2
    yield so1
    yield so2
A=[]
for i in so(x,y):
    A.append(i)
print(A)