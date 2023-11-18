s=input()
b=''
for i in range(len(s)-1,-1,-1):
    b=b+s[i]
if b==s:
    print('co')
else:
    print('khong')