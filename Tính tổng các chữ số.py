n=float(input())
s=0
while n>0:
    dv=n%10
    n=n//10
    s=s+dv
print(s)