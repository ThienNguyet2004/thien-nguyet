a=float(input("nhap gia tri thu nhat la :"))
b=float(input("nhap gia tri thu hai la :"))
c=float(input("nhap gia tri thu ba la :"))
S1=a*a-2*b+(a*b)/(c*c+3)
S2=(b*b-4*a*c)/(2*a)
import math
S3=3*a-b**3+2*math.sqrt(c*c+1)
S4=math.sqrt(a*a/b-4*(a/(b*c))+1)
x1=format(S1,".3f")
x2=format(S2,".3f")
x3=format(S3,".3f")
x4=format(S4,".3f")
print("ket qua cua bieu thuc mot la : ",x1)
print("ket qua cua bieu thuc hai la : ",x2)
print("ket qua cua bieu thuc ba la : ",x3)
print("ket qua cua bieu thuc bon la : ",x4)