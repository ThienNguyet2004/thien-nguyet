s=1
tong=0
for i in range(1,6):
    m=i
    for j in range(1,(2*m-1)+1):
        s*=j
        print('luythua',s)
    
    bieuthuc=((-1)**(m-1))*(3.5**(2*m-1)/s)
    print(bieuthuc)
    tong+=bieuthuc
    s=1
print(tong)
