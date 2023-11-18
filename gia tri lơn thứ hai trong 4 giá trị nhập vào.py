a=int(input())
b=int(input())
c=int(input())
d=int(input())
list=[a,b,c,d]
list.sort()
m=list[-1]
if (a==b==c==d):
    print(m)
else:
    def check_max(m):
       if max(list)==m:
          return True
       else :
          return False
    while check_max(m):
          list.remove(m)
    print(max(list))