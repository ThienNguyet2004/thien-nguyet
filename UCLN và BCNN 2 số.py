x=int(input())
y=int(input())
def ucln(x,y):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    ucln=x
    return ucln
def bcnn(ucln,x,y):
    bcnn=int((x*y)/ucln(x,y))
    return bcnn
print(ucln(x,y))
print(bcnn(ucln,x,y))