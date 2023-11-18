def nhap_du_lieu():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    return a,b,c,d
def tim_max(a,b,c,d):
    max=a
    if a<b:
        max=b
    if b<c:
        max=c
    if c<d:
        max=d
    return max

def tim_BCNN(a,b,c,d,max):
    while True :
        if (max%a==0 and max%b==0 and max%c==0 and max%d==0):
            bcnn=max
            break
        max+=1
    return bcnn

a,b,c,d=nhap_du_lieu()
max=tim_max(a,b,c,d)
print(tim_BCNN(a,b,c,d,max))
    