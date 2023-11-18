n=int(input())
#Hàm tính thứ tự của số
def kt_co_may_chu_so(n):
    x = 0
    while(n!=0) :
        x += 1
        n = n//10
    return x
print(kt_co_may_chu_so(n))