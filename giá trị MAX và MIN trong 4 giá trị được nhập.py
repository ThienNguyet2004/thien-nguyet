a=int(input())
b=int(input())
c=int(input())
d=int(input())
def find_max(a,b,c,d):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    if max<d:
        max=d
    return max
def find_min(a,b,c,d):
    min=d
    if min>c:
        min=c
    if min>b:
        min=b
    if min>a:
        min=a
    return min
print('gia tri nho nhat la:',find_min(a,b,c,d))
print('gia tri lon nhat la:',find_max(a,b,c,d))