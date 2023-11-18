#so phut goi la x
x=int(input())
#tien cuoc goi la y
if (0<=x<=50):
    y=150000+x*600
    print(y)
elif (51<=x<=200):
    y=150000+50*600+(x-50)*400
    print(y)
else :
    y=150000+50*600+150*400+(x-200)*200
    print(y)