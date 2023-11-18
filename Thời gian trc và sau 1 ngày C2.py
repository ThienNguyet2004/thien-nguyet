ngay=int(input())
thang=int(input())
nam=int(input())
from datetime import date,timedelta
t0=date(nam,thang,ngay)
t1=t0-datetime(days=1)
t2=t0+timedelta(days=1)
print(t1.strftime("%d/%m/%Y"))
print(t2.strftime("%d/%m/%Y"))