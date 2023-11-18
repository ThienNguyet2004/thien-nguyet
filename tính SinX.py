x=float(input())
m=int(input())
#tinh bieu thuc:
#sinx=x - pow(x,3)/3! + pow(x,5) +...+ pow(-1,m-1)*pow(x,2*m-1)/(2*m-1)!
def tinh_sinx(x,m):
    tong=0
    s=1
    for i in range(1,m+1):
        mu=2*i-1
        for j in range(1,mu+1):
            s*=j            
        sinx=((-1)**(i-1))*((x**mu)/s)
        tong+=sinx
        s=1
    return tong    
print(f'{tinh_sinx(x,m):.3f}')


    
    