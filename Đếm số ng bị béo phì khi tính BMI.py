n=int(input())
chieucao=[]
cannang=[]
count=0
for i in range(n):
    x=float(input())
    y=float(input())
    chieucao.append(x)
    cannang.append(y)
    bmi=cannang[i]/(chieucao[i])**2
    if bmi<18.5:
        continue
    elif 18.5<=bmi<25:
        continue
    elif 25<=bmi<30:
        continue
    elif bmi>=30:
        count+=1
print(count)