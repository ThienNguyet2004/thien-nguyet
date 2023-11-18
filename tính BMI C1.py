ten=input('ho ten cua ban la:')
chieucao=float(input('chieu cao cua ban la (m) :'))
cannang=float(input('can nang cua ban la (kg) :'))
BMI=cannang/chieucao**2
x=float(format(BMI,".3f"))
print('ban',ten,'co chi so BMI la:',x)
if (18.5<=x<=25):
    print('suc khoe binh thuong')
elif (x<18.5):
    print('ban gay')
elif (25<=x<=30):
    print('thua can')
else :
    print('ban dang beo phi')
        
        